from rest_framework import authentication
from fgnbfhvc.models import Tgjf
from .serializers import TgjfSerializer
from rest_framework import viewsets


class TgjfViewSet(viewsets.ModelViewSet):
    serializer_class = TgjfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Tgjf.objects.all()
