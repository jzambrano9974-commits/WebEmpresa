from django.urls import path
from core import views

urlpatterns = [
    path('', views.services, name='services'),
]