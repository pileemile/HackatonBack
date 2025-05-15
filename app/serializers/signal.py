from rest_framework import serializers
from app.models import Signal


class SignalSerializer(serializers.Serializer):
    class Meta:
        model = Signal
        fields = ('id', 'name', 'description')