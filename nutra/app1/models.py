from django.db import models
from django.utils import timezone

class SensorData(models.Model):
    temperature = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Temperature in °C"
    )
    humidity = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Humidity in %"
    )
    pressure = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        help_text="Pressure in PA"
    )
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"Sensor Data at {self.timestamp}"
    
    
