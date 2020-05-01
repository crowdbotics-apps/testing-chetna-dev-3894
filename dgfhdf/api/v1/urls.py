from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FfgjyViewSet

router = DefaultRouter()
router.register("ffgjy", FfgjyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
