from rest_framework import serializers
from uav.models import UAV

# Serializer for UAV
class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'
