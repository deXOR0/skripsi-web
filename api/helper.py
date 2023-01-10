from datetime import datetime
from typing import List
from dashboard.helper import ISPU
import pytz

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
            pm25_lower_limit = pm25_value_list[max(0, i-1)] if pm25_value_list[i] != pm25_value_list[-1] else pm25_value_list[-1]
            ispu_upper_limit = ISPU[i]['max']
            ispu_lower_limit = ISPU[max(0, i-1)]['max'] if pm25_value_list[i] != pm25_value_list[-1] else ISPU[-1]['max']
            break

    ispu = (((ispu_upper_limit - ispu_lower_limit) / (pm25_upper_limit - pm25_lower_limit)) * (avg_value - pm25_lower_limit)) + ispu_lower_limit

    return int(round(ispu))

