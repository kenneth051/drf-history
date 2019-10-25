from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Users(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)


class Todo(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    action = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
