from rest_framework import serializers
from app.models import SignalActivity


class SignalActivitySerializer (serializers.ModelSerializer):
    class Meta:
        model = SignalActivity
        fields = ('id', 'signal', 'date', 'type')