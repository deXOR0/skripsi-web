from django.shortcuts import render

# Create your views here.
def co_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'active': 'co'})

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