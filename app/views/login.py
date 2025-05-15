from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import authenticate
from app.serializers.users import UserSerializer


class CustomAuthToken(ObtainAuthToken):
    class AuthTokenSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    def post(self, request, *args, **kwargs):
        serializer = self.AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Authentification par username (ou email si modifié)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user is None:
            return Response({"detail": "Invalid credentials"}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })
