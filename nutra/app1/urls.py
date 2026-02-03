from django.urls import path
from . import views  # Ensure you're importing views properly


urlpatterns = [
    path('sensor_data/', views.SensorDataCreateView.as_view(), name='sensor-data-create'),  
    path('', views.sensor_dashboard, name='sensor_dashboard'),  
    path('delete-sensor-data/', views.delete_sensor_data, name='delete_sensor_data'),

] 