from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from dotenv import load_dotenv
from .models import ISPU
from datetime import datetime
from .helper import utc_to_local
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
            if json_data['api_key'] == os.environ['API_KEY']:

                ispu = ISPU.objects.all()

                now = datetime.now(pytz.utc)

                if len(ispu) > 0:
                    ispu_timestamp = ispu[0].timestamp
                    if ispu_timestamp.date() == now.date() and ispu_timestamp.hour == now.hour:
                        msg = f'update not performed since ispu data already exists for {utc_to_local(ispu_timestamp)}'
                        return JsonResponse({
                            'status': 'false',
                            'message': msg
                        })

                ISPU.objects.all().delete()
                new_ispu = ISPU(value=21)
                new_ispu.save()

                return JsonResponse({
                    'status': 'true',
                    'message': str(new_ispu)
                })
            else:
                return JsonResponse(status=403, data={'status': 'false', 'message': 'invalid API key'})
        except Exception as e:
            print(e)
            return JsonResponse(status=400, data={'status': 'false', 'message': 'malformed request body'})
    else:
        return JsonResponse(status=405, data={'status': 'false', 'message': 'method not allowed'})