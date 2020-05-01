from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FfghuViewSet

router = DefaultRouter()
router.register("ffghu", FfghuViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
