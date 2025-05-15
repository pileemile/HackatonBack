from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.models import Signal
from app.serializers import SignalSerializer


class SignalModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = SignalSerializer

    def get_queryset(self):
        return Signal.objects.all()