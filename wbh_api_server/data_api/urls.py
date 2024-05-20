# data_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('safe_tip/', views.safe_tip, name='safe_tip'),
    path('cctv_in_radius/', views.cctv_coordinates_in_radius, name='cctv_in_radius'),
    path('convenience_in_radius/', views.conveniencestore_coordinates_in_radius, name='convenience_in_radius'),
    path('policestation_in_radius/', views.policestation_coordinates_in_radius, name='policestation_in_radius'),
    path('alarmbell_in_radius/', views.alarmbell_coordinates_in_radius, name='alarmbell_in_radius'),
]

