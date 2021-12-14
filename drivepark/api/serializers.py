from django.db.models.fields import DateField
from rest_framework import serializers

from .models import Vehicle, Driver

class DriverSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)
  #  first_name = serializers.CharField(required=True, allow_blank=False, max_length=40)
   # last_name = serializers.CharField(required=True, allow_blank=False, max_length=40)

    class Meta:
        model = Driver
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class FilterSerializer(serializers.Serializer):
    dt_url=serializers.DateField()
    class Meta:
       # model = Driver
        fields = '__all__'

