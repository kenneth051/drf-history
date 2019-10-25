from rest_framework import authentication, exceptions
from app_test.models import Users
import jwt
from django.conf import settings


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return None
        try:
            payload = self.decode_token(token)
            user = Users.objects.get(username=payload["username"])
            return (user, payload)
        except Exception:
            raise exceptions.AuthenticationFailed("User doesnt exist")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            raise exceptions.AuthenticationFailed("The token is invalid")

        return payload
