from django.db import models
from django.utils import timezone


# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=timezone.now)
