# data_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('coord_test/', views.coord_tester, name='coord_test'),
]

