from rest_framework import authentication
from dgfhdf.models import Ffgjy
from .serializers import FfgjySerializer
from rest_framework import viewsets


class FfgjyViewSet(viewsets.ModelViewSet):
    serializer_class = FfgjySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ffgjy.objects.all()
