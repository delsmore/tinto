from rest_framework import serializers
from helios.models import Service


class ServiceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Service
        depth = 1
