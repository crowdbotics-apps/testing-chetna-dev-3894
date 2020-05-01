from rest_framework import authentication
from fgdh.models import Gxfghtgf
from .serializers import GxfghtgfSerializer
from rest_framework import viewsets


class GxfghtgfViewSet(viewsets.ModelViewSet):
    serializer_class = GxfghtgfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Gxfghtgf.objects.all()
