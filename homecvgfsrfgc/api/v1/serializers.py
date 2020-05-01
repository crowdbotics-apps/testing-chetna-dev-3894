from rest_framework import serializers
from homecvgfsrfgc.models import Ffghu


class FfghuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ffghu
        fields = "__all__"
