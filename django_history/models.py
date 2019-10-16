from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from django_history import constants


class History(models.Model):
    table_name = models.CharField(max_length=255, blank=False, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    instance_id = models.CharField(
        max_length=255, null=False, blank=False, editable=False
    )
    action = models.CharField(
        max_length=7,
        null=False,
        blank=False,
        choices=constants.django_history,
        editable=False,
    )
    request_data = models.TextField(default="", editable=False)
    response_data = models.TextField(default="", editable=False)

    class Meta:
        verbose_name_plural = "History model"
