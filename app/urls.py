from rest_framework.routers import SimpleRouter
from django.urls import include, path

from app.views import CustomAuthToken, SignalModelViewSet, SignalActivityModelViewSet, PropActivityViewSet

router = SimpleRouter()

router.register("signal", SignalModelViewSet, basename="signal")
router.register("signalActivity", SignalActivityModelViewSet, basename="signalActivity")
router.register("propActivity", PropActivityViewSet, basename="propActivity")

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", CustomAuthToken.as_view()),
]