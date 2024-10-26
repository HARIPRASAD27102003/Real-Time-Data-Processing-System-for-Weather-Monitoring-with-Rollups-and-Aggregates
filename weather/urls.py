from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_weather_data/', views.fetch_weather_data, name='fetch_weather_data'),
    path('temperature_stats/', views.temperature_stats, name='temperature_stats'),
    path('set_threshold/', views.set_threshold, name='set_threshold'),
]
