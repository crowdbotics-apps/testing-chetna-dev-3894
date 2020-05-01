from rest_framework import serializers
from srfwe.models import Feeaa


class FeeaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeaa
        fields = "__all__"
