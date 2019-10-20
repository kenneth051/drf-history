from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Todo(models.Model):
    todo=models.CharField(max_length=255)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
