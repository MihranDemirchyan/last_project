from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.username}"
