from rest_framework import authentication
from homecvgfsrfgc.models import Ffghu
from .serializers import FfghuSerializer
from rest_framework import viewsets


class FfghuViewSet(viewsets.ModelViewSet):
    serializer_class = FfghuSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ffghu.objects.all()
