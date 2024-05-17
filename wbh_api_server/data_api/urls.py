# data_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('coord_test/', views.coord_tester, name='coord_test'),
    path('coordinates_in_radius/', views.cctv_coordinates_in_radius, name='cctv_coordinates_in_radius'),
]

