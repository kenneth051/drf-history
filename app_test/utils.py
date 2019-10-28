from django.conf import settings
from datetime import datetime, timedelta
import jwt


def token(user):
    credentials = {
        "id": user.id,
        "username": user.username,
        "is_staff": user.is_staff,
        "exp": datetime.now() + timedelta(days=1),
    }
    return jwt.encode(credentials, settings.SECRET_KEY).decode("utf-8")
