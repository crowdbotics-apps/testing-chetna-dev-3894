from django.conf import settings
from django.db import models


class Tgjf(models.Model):
    "Generated Model"
    cfgsf = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tgjf_cfgsf",
    )


# Create your models here.
