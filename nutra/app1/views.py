from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny  # For simplicity; adjust for authentication if needed
from .models import *
from .serializers import *



# Dashboard View for displaying all sensor data
def sensor_dashboard(request):
    sensor_data = SensorData.objects.all()  # Retrieve all records
    return render(request, 'app1/dashboard.html', {'sensor_data': sensor_data})

# API View for POST (creating new sensor data)
class SensorDataCreateView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]  # Allows anyone to POST; secure this in production

from django.shortcuts import redirect
from django.contrib import messages
from .models import SensorData

def delete_sensor_data(request):
    if request.method == "POST":
        ids = request.POST.getlist('selected_ids')

        if ids:
            SensorData.objects.filter(id__in=ids).delete()
            messages.success(request, "Selected records deleted successfully.")
        else:
            messages.warning(request, "No records selected.")

    return redirect('sensor_dashboard')
