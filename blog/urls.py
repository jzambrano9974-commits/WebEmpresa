from django.urls import path
from core import views

urlpatterns = [
    # Aquí le devolvemos el nombre 'blog'
    path('', views.blog, name='blog'),
]