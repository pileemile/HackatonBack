from rest_framework import serializers

from app.models import PropActivity


class PropActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropActivity
        fields = ("id", "titre", "description")