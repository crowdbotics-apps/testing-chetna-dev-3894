from rest_framework import serializers
from dgfhdf.models import Ffgjy


class FfgjySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ffgjy
        fields = "__all__"
