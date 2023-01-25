from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.db.models import Avg
from dotenv import load_dotenv
from .models import ISPU, RecentPollutant
from dashboard.models import Pollutant, Timestamp
from datetime import datetime, timedelta
from .helper import utc_to_local, calculate_ispu, predict
import os
import json
import pytz

load_dotenv()

# Create your views here.

@sensitive_post_parameters('api_key')
@csrf_exempt
def update_ispu(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            _ = json_data['api_key'] == os.environ['API_KEY']
        except:
            return JsonResponse(status=400, data={'status': 'false', 'message': 'malformed request body'})
        if json_data['api_key'] == os.environ['API_KEY']:

            print('==============================')
            started = datetime.now()
            print(started)
            print('Started ISPU calculation')

            ispu = ISPU.objects.all()

            now = datetime.now(pytz.utc).replace(minute=1, second=0, microsecond=0)

            if len(ispu) > 0:
                ispu_timestamp = ispu[0].timestamp
                if ispu_timestamp.date() == now.date() and ispu_timestamp.hour == now.hour:
                    msg = f'update not performed since ispu data already exists for {utc_to_local(ispu_timestamp)}'
                    return JsonResponse({
                        'status': 'false',
                        'message': msg
                    })


            timestamps = Timestamp.objects.filter(timestamp__range=[now - timedelta(hours=24), now]).order_by('timestamp')
            pm25 = []
            for timestamp in timestamps:
                data = Pollutant.objects.filter(timestamp=timestamp).select_related().values_list('pm25')
                pm25.append(data.aggregate(Avg('pm25'))['pm25__avg'])
                
            new_ispu_value = calculate_ispu(pm25)

            ISPU.objects.all().delete()

            new_ispu = ISPU(value=new_ispu_value)
            new_ispu.save()

            ended = datetime.now()
            print('ISPU update done.')
            print(f'Took {ended-started}')
            print('==============================')

            return JsonResponse({
                'status': 'true',
                'message': str(new_ispu)
            })
        else:
            return JsonResponse(status=403, data={'status': 'false', 'message': 'invalid API key'})
    else:
        return JsonResponse(status=405, data={'status': 'false', 'message': 'method not allowed'})

@sensitive_post_parameters('api_key')
@csrf_exempt
def update_prediction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            _ = json_data['api_key'] == os.environ['API_KEY']
        except:
            return JsonResponse(status=400, data={'status': 'false', 'message': 'malformed request body'})

        if json_data['api_key'] == os.environ['API_KEY']:

            print('==============================')
            started = datetime.now()
            print(started)
            print('Started prediction')

            recent_pollutants = RecentPollutant.objects.order_by('timestamp')

            now = datetime.now(pytz.utc).replace(minute=1, second=0, microsecond=0)

            if len(recent_pollutants) > 0:
                recent_pollutant_timestamp = recent_pollutants[11].timestamp
                if recent_pollutant_timestamp.date() == now.date() and recent_pollutant_timestamp.hour == now.hour:
                    msg = f'update not performed since prediction data already exists for {utc_to_local(recent_pollutant_timestamp)}'
                    return JsonResponse({
                        'status': 'false',
                        'message': msg
                    })

            RecentPollutant.objects.all().delete()

            timestamps = Timestamp.objects.filter(timestamp__range=[now - timedelta(hours=12), now]).order_by('timestamp')

            duplicate_timestamp = duplicate_pm25 = None

            for timestamp in timestamps:
                data = Pollutant.objects.filter(timestamp=timestamp).select_related().values_list('pm25')
                new_pm25 = round(data.aggregate(Avg('pm25'))['pm25__avg'], 2)
                new_entry = RecentPollutant(timestamp=timestamp.timestamp, pm25=new_pm25, _type='real')
                duplicate_timestamp = timestamp.timestamp
                duplicate_pm25 = new_pm25
                new_entry.save()
            
            duplicate = RecentPollutant(timestamp=duplicate_timestamp, pm25=duplicate_pm25, _type='predicted')
            duplicate.save()

            predictions = predict()

            for index, row in predictions.iterrows():
                new_entry = RecentPollutant(timestamp=index, pm25=row['predicted_mean'], _type='predicted')
                new_entry.save()

            ended = datetime.now()
            print('Prediction update done.')
            print(f'Took {ended-started}')
            print('==============================')

            return JsonResponse({
                'status': 'true',
                'message': str(predictions)
            })
        else:
            return JsonResponse(status=403, data={'status': 'false', 'message': 'invalid API key'})
    else:
        return JsonResponse(status=405, data={'status': 'false', 'message': 'method not allowed'})