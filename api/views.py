from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.db.models import Avg
from dotenv import load_dotenv
from .models import ISPU
from dashboard.models import Pollutant, Timestamp
from datetime import datetime, timedelta
from .helper import utc_to_local, calculate_ispu
import os
import json
import pytz
import traceback

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

            print(new_ispu)

            return JsonResponse({
                'status': 'true',
                'message': str(new_ispu)
            })
        else:
            return JsonResponse(status=403, data={'status': 'false', 'message': 'invalid API key'})
    else:
        return JsonResponse(status=405, data={'status': 'false', 'message': 'method not allowed'})