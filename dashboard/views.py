from django.shortcuts import render
from datetime import datetime
from .helper import ISPU, day_of_week, month, transform_to_class_name
from api.models import ISPU as ISPU_model
from api.helper import JAKARTA
import pytz

# Create your views here.
def dashboard(request):
    ispu = ISPU_model.objects.all()[0].value
    ispu_data = {}
    for i in ISPU:
        if ispu >= i['min'] and ispu <= i['max']:
            ispu_data['value'] = ispu
            ispu_data['emoji'] = i['emoji']
            ispu_data['category'] = i['category']
            ispu_data['class'] = transform_to_class_name(i['category'])
            ispu_data['description'] = i['description']
            break

    date = datetime.now().astimezone(JAKARTA)
    formatted_date = f'{day_of_week[date.weekday()]}, {date.day} {month[date.month-1]}'

    return render(request, 'dashboard/dashboard.html', {'ispu': ispu_data, 'date': formatted_date})