from rest_framework import authentication
from srfwe.models import Feeaa
from .serializers import FeeaaSerializer
from rest_framework import viewsets


class FeeaaViewSet(viewsets.ModelViewSet):
    serializer_class = FeeaaSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Feeaa.objects.all()
