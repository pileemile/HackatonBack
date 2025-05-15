from rest_framework.routers import SimpleRouter
from django.urls import include, path

from app.views import CustomAuthToken

router = SimpleRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", CustomAuthToken.as_view()),
]