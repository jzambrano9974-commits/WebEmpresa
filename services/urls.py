from django.urls import path
from core import views

urlpatterns = [
    # Aquí le devolvemos el nombre 'services' para que el botón lo encuentre
    path('', views.services, name='services'),
]