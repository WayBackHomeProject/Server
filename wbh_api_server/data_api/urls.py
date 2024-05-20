# data_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('coord_test/', views.coord_tester, name='coord_test'),
    path('cctv_in_radius/', views.cctv_coordinates_in_radius, name='cctv_in_radius'),
    path('convenience_in_radius/', views.conveniencestore_coordinates_in_radius, name='convenience_in_radius'),
    path('policestation_in_radius/', views.policestation_coordinates_in_radius, name='policestation_coordinates_in_radius'),
]

