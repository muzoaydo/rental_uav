from rest_framework import serializers
from django.forms import ModelForm
from uav.models import UAV

# Serializer for UAV
class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'

class UAVForm(ModelForm):
    class Meta:
        model = UAV
        fields = '__all__'
