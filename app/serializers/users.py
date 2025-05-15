from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #hash le mot de passe
    def create(self, validated_data):
        raw_password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(raw_password)
        user.save()
        return user