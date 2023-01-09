"""skripsi_aqf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/co', permanent=True)),
    path('co', dashboard_views.co_dashboard, name='co'),
    path('no2/', dashboard_views.no2_dashboard, name='no2'),
    path('o3/', dashboard_views.o3_dashboard, name='o3'),
    path('pm10/', dashboard_views.pm10_dashboard, name='pm10'),
    path('pm25/', dashboard_views.pm25_dashboard, name='pm25'),
    path('so2/', dashboard_views.so2_dashboard, name='so2'),
]
