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
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.dashboard, name='dashboard'),
    path('api/update-ispu', api_views.update_ispu, name='update_ispu'),
    path('api/update-prediction', api_views.update_prediction, name='update_prediction'),
]
