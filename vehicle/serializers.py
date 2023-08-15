from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = serializers.ChoiceField(choices=Vehicle.vehicle_type_choices)

    class Meta:
        model = Vehicle
        fields = '__all__'
