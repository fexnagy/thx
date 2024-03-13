from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Room(models.Model):
    COUNTRY_CHOICES = [
        ("NL", "Netherlands"),
        ("BE", "Belgium"),
        ("DE", "Germany"),
        ("FR", "France"),
        ("UK", "United Kingdom"),
    ]
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default="NL")
    name_client = models.CharField(max_length=50, default="")
    name_advertiser = models.CharField(max_length=50, null=True, blank=True, default="")
    name_campaign = models.CharField(max_length=50, default="")
    comment = models.TextField(max_length=100, null=True, blank=True, default="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name_client


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
