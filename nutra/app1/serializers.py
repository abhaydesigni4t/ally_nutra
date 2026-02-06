from rest_framework import serializers
from .models import *

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'temperature', 'humidity', 'pressure', 'timestamp']
        read_only_fields = ['id', 'timestamp']
        extra_kwargs = {
            'temperature': {'required': False},
            'humidity': {'required': False},
            'pressure': {'required': False},
        }