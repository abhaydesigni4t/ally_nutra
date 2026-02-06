from django.db import models
from django.utils import timezone
import pytz

EST = pytz.timezone('America/New_York')

def get_est_time():
    return timezone.now().astimezone(EST)

class SensorData(models.Model):
    temperature = models.DecimalField(
        max_digits=5, 
        decimal_places=2,  
        help_text="Temperature in °C",
        null=True,  # Allow NULL in database
        blank=True  # Allow empty in forms/serializers
    )
    humidity = models.DecimalField(
        max_digits=5, 
        decimal_places=2,  
        help_text="Humidity in %",
        null=True,
        blank=True
    )
    pressure = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        help_text="Pressure in PA",
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(default=get_est_time)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"Sensor Data at {self.timestamp}"