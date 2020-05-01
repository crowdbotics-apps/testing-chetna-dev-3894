from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FeeaaViewSet

router = DefaultRouter()
router.register("feeaa", FeeaaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
