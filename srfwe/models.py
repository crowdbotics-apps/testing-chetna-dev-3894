from django.conf import settings
from django.db import models


class Feeaa(models.Model):
    "Generated Model"
    adfger = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feeaa_adfger",
    )


# Create your models here.
