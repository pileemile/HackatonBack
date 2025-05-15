from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.models import SignalActivity
from app.serializers import SignalActivitySerializer


class SignalActivityModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = SignalActivitySerializer
    def get_queryset(self):
        return SignalActivity.objects.all()