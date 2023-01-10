from django.shortcuts import render
from datetime import datetime
from .helper import ISPU, day_of_week, month, transform_to_class_name
from api.models import ISPU as ISPU_model

# Create your views here.
def co_dashboard(request):
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

    date = datetime.now()
    formatted_date = f'{day_of_week[date.weekday()]}, {date.day} {month[date.month-1]}'

    return render(request, 'dashboard/dashboard.html', {'active': 'co', 'ispu': ispu_data, 'date': formatted_date})

def no2_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'no2'})

def o3_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'o3'})

def pm10_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'pm10'})
    
def pm25_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'pm25'})
    
def so2_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'so2'})