from rest_framework import serializers
from app.models import Signal


class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = ('id', 'name', 'description')