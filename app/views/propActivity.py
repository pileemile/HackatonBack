from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.models import PropActivity
from app.serializers import PropActivitySerializer


class PropActivityViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PropActivitySerializer

    def get_queryset(self):
        return PropActivity.objects.all()