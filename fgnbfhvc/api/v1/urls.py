from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TgjfViewSet

router = DefaultRouter()
router.register("tgjf", TgjfViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
