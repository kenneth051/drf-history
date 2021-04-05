import os

# yaml
import yaml
from yaml import Loader

# django Imports
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings

# App Imports
from track_actions.constants import TABLES
from track_actions.models import History
from track_actions.requestMiddleware import RequestMiddleware

# python imports
import datetime
import json


@receiver(post_save)
@receiver(post_delete)
def track_user_actions(sender, instance, **kwargs):
    """Signal function to track every change to a model

    Arguments:
        sender {object} -- The model sending the signal
        instance {object} -- data instance
    """
    current_request = RequestMiddleware.get_request_data()[1]
    if (
        sender._meta.db_table not in TABLES
        and hasattr(current_request, "user")
        and hasattr(instance, "id")
    ):
        if RequestMiddleware.get_request_data()[0]:
            request_data = decode_json(RequestMiddleware.get_request_data()[0])
        else:
            request_data = ""
        data = instance.__dict__.copy()
        data.__delitem__("_state")
        if "drf_history.yaml" in os.listdir(settings.BASE_DIR):
            yaml_file = open(settings.BASE_DIR + "/drf_history.yaml", "r")
            yaml_content = yaml.load(yaml_file, Loader=Loader)
            if (
                type(yaml_content) is dict
                and type(request_data) is dict
                and "fields_to_exclude" in yaml_content.keys()
                and type(yaml_content["fields_to_exclude"]) is list
            ):
                feilds_to_exclude = yaml_content["fields_to_exclude"]
                [request_data.pop(key, None) for key in feilds_to_exclude]

        save_history(instance, current_request, request_data, data)


def decode_json(data):
    request_data = ""
    try:
        request_data = json.loads(data)
    except:
        pass
    return request_data


def save_history(instance, current_request, request_data, data):
    try:
        history = History(
            table_name=str(instance._meta.db_table),
            user=current_request.user,
            instance_id=instance.id,
            action=current_request.method,
            request_data=request_data,
            path=current_request.path,
            response_data=data,
        )
        history.save()
    except ValueError:
        pass