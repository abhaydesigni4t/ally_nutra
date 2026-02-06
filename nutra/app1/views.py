from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny  # For simplicity; adjust for authentication if needed
from .models import *
from .serializers import *



# Dashboard View for displaying all sensor data
def sensor_dashboard(request):
    sensor_data = SensorData.objects.all()

    est = pytz.timezone('America/New_York')

    for data in sensor_data:
        data.timestamp_est = data.timestamp.astimezone(est)

    return render(request, 'app1/dashboard.html', {'sensor_data': sensor_data})

# API View for POST (creating new sensor data)
class SensorDataCreateView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]  # Allows anyone to POST; secure this in production

from django.shortcuts import redirect
from django.contrib import messages
from .models import SensorData

from django.db import connection, transaction
from django.conf import settings

def delete_sensor_data(request):
    if request.method == "POST":
        ids = request.POST.getlist('selected_ids')
        
        # Validate IDs (basic check: ensure they are integers)
        try:
            ids = [int(id) for id in ids if id.isdigit()]
        except ValueError:
            messages.error(request, "Invalid IDs provided.")
            return redirect('sensor_dashboard')
        
        if ids:
            with transaction.atomic():  # Ensure atomicity
                SensorData.objects.filter(id__in=ids).delete()
                
                # Check if table is now empty and reset sequence
                if not SensorData.objects.exists():
                    db_engine = settings.DATABASES['default']['ENGINE']
                    table_name = SensorData._meta.db_table  # e.g., 'app1_sensordata'
                    
                    with connection.cursor() as cursor:
                        if 'postgresql' in db_engine:
                            cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1;")
                        elif 'sqlite3' in db_engine:
                            cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}';")
                        elif 'mysql' in db_engine:
                            cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
                        # Add other DBs if needed
                    
                    messages.success(request, "All records deleted and ID sequence reset.")
                else:
                    messages.success(request, "Selected records deleted successfully.")
        else:
            messages.warning(request, "No records selected.")
    
    return redirect('sensor_dashboard')

