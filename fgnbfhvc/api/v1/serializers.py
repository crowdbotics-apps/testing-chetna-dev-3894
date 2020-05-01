from rest_framework import serializers
from fgnbfhvc.models import Tgjf


class TgjfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tgjf
        fields = "__all__"
