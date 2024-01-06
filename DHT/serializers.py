from rest_framework import serializers
from .models import Dht11


class DHT11Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dht11
        fields = '__all__'


class DHT11serialize:
    pass