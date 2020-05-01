from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    gfg = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_gfg",
    )
    hghg = models.ManyToManyField(
        "home.CustomText", blank=True, related_name="customtext_hghg",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    hghgh = models.OneToOneField(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_hghgh",
    )
    jhj = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_jhj",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
