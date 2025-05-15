from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.models import SignalActivity


class SignalActivityModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    def get_queryset(self):
        return SignalActivity.objects.all()