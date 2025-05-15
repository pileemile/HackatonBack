from rest_framework import serializers

from app.models import PropActivity


class PropActivitySerializer(serializers.Serializer):
    class Meta:
        model = PropActivity
        field = ("id", "titre", "description")