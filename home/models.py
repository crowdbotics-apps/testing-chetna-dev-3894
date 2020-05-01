from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    abc = models.ManyToManyField("users.User", blank=True, related_name="homepage_abc",)
    gfgf = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_gfgf",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
