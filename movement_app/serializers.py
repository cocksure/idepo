from rest_framework import serializers
from .models import Outgoing, Incoming


class IncomingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoming
        fields = '__all__'


class OutgoingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outgoing
        fields = '__all__'
