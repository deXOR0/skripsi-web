from datetime import datetime, timedelta
from typing import List
from dashboard.helper import ISPU
from statsmodels.tsa.statespace import sarimax
from django.db import connection
import pandas as pd
import numpy as np
import pytz

K = 10
UTC = pytz.timezone("utc") 

def utc_to_local(utc_dt):
    tz = pytz.timezone('Asia/Jakarta')
    utc_dt = utc_dt.replace(tzinfo=pytz.UTC)
    
    return utc_dt.astimezone(tz)

def calculate_ispu(pollutant: List[float]) -> int:
    avg_value = sum(pollutant) / len(pollutant)
    ispu_upper_limit = ispu_lower_limit = 0
    pm25_upper_limit = pm25_lower_limit = 0

    pm25_value_list = [x[list(x.keys())[2]] for x in ISPU]


    for i in range(len(pm25_value_list)):
        if avg_value <= pm25_value_list[i]:
            pm25_upper_limit = pm25_value_list[i]
            ispu_upper_limit = ISPU[i]['max']
            if i == 0:
                pm25_lower_limit = 0
                ispu_lower_limit = 0
            else:
                pm25_lower_limit = pm25_value_list[i-1] if pm25_value_list[i] != pm25_value_list[-1] else pm25_value_list[-1]
                ispu_lower_limit = ISPU[i-1]['max'] if pm25_value_list[i] != pm25_value_list[-1] else ISPU[-1]['max']
            break

    print(f'{avg_value=}, {ispu_upper_limit=}, {ispu_lower_limit=}, {pm25_upper_limit=}, {pm25_lower_limit=}, {pm25_value_list=}')
    ispu = (((ispu_upper_limit - ispu_lower_limit) / (pm25_upper_limit - pm25_lower_limit)) * (avg_value - pm25_lower_limit)) + ispu_lower_limit

    return int(round(ispu))

def predict():

    now = datetime.now(UTC).replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    end = now + timedelta(hours=11)

    db_df = fetch_dataset()
    df = preprocess(db_df)

    df.set_index('time_stamp', inplace=True)

    train_df = df['pm25']

    exog = generate_exog(df)

    prediction_df = pd.DataFrame(index=pd.date_range(start=now, end=end, freq='H'))

    test_exog = generate_exog(prediction_df)

    sarimax_model = sarimax.SARIMAX(train_df, exog=exog, order=(2, 1, 0), seasonal_order=(2, 0, 0, 24)).fit()

    prediction = sarimax_model.predict(start=now, end=end, exog=test_exog).round(2)

    prediction = prediction.to_frame()

    prediction = prediction.set_index(prediction.index.tz_convert('Asia/Jakarta'))

    return prediction

def generate_exog(df):
    exog = pd.DataFrame({'date': df.index})
    exog = exog.set_index(pd.DatetimeIndex(exog['date'], freq='H'))
    exog['sin7_2'] = np.sin(K * np.pi * exog.index.dayofweek / 7)
    exog['cos7_2'] = np.cos(K * np.pi * exog.index.dayofweek / 7)
    exog = exog.drop(columns=['date'])

    return exog
    

def preprocess(df):
    df.drop_duplicates(inplace=True)

    no_duplicate_df = df.groupby(['time_stamp', 'district']).agg({'pm25':'mean'}).reset_index()

    complete_timestamps = generate_timestamps(start=no_duplicate_df['time_stamp'].tolist()[1], end=no_duplicate_df['time_stamp'].tolist()[-1], df=no_duplicate_df)

    dict_of_district_df = generate_df_by_district(no_duplicate_df)

    missingg_timestamps_df = pd.DataFrame(data=[{'time_stamp': t, 'pm25': None} for t in complete_timestamps if t not in set(no_duplicate_df.time_stamp.unique())])

    for district, district_df in dict_of_district_df.items():
        dict_of_district_df[district] = pd.concat([district_df, missingg_timestamps_df], ignore_index=True).sort_values(['time_stamp'])
        dict_of_district_df[district]['district'] = dict_of_district_df[district]['district'].fillna(district)
    
    for district, district_df in dict_of_district_df.items():
        dict_of_district_df[district]['pm25'].interpolate(method='linear', limit_direction='both', axis=0, inplace=True)
    
    cleaned_df = None
    for idx, (district, district_df) in enumerate(dict_of_district_df.items()):
        if idx == 0: 
            cleaned_df = district_df 
            continue
        cleaned_df = pd.concat([cleaned_df, district_df], ignore_index=True).sort_values(['time_stamp'])
    
    roled_up_df = roll_up_data(cleaned_df).round(2)

    print("Preprocessing done")

    return roled_up_df

def fetch_dataset():
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT 
            t.timestamp,
            p.pm25,
            d.district_name,
            c.city_name
        FROM
            pollutants p
                JOIN
            timestamps t
                ON p.timestamp_id= t.time_id
                JOIN
            districts d
                ON d.district_id = p.district_id
            JOIN cities c
                ON c.city_id = d.city_id
        ORDER BY t.timestamp ASC
        ''')

        records = cursor.fetchall()

        df = pd.DataFrame(data=records, columns=('time_stamp', 'pm25', 'district', 'city'))

        print("Dataset fetching done")
        
        return df

def generate_timestamps(start, end, df):
    start_orig = start
    start = start.replace(hour=0, minute=0, second=0)
    timestamps = []

    end = df['time_stamp'].iloc[-1]

    for day in range(0, (end-start).days+1):
        new_day = start + timedelta(days=day)
        for hour in range(0, 24):
            new_timestamp = start + timedelta(days=day, hours=hour)
            if (new_timestamp.date() == new_day.date()):
                timestamps.append(new_timestamp)
            else:
                break
    
    timestamps = timestamps[timestamps.index(start_orig):timestamps.index(end)+1]
    return timestamps

def generate_df_by_district(df):
    # memisahkan df berdasarkan kecamatan dan memasukkannya ke dalam dictionary 
    temp_df = df.copy()
    df_by_districts = {}
    for district in temp_df.district.unique():
        indexes = temp_df[temp_df['district']==district].index.values
        df_by_districts[district] = temp_df.loc[indexes]
    return df_by_districts

def roll_up_data(df):
    """
    Roll up data dengan melakukan grouping sehingga level data menjadi tingkat DKI Jakarta
    parameter:
        - df: data obtained from postgresql in pandas dataframe form
    return: 
    """
    return df.groupby('time_stamp').agg({'pm25':'mean'}).reset_index()