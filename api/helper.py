from datetime import datetime
import pytz

def utc_to_local(utc_dt):
    tz = pytz.timezone('Asia/Jakarta')
    utc_dt = utc_dt.replace(tzinfo=pytz.UTC)
    
    return utc_dt.astimezone(tz)