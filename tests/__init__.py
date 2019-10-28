from django.test import TestCase, Client

from django.contrib.auth.models import User
from app_test.models import Users


class BaseTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Users(username="testuser", is_staff=True, email="test@test.com")
        self.user.set_password("ken12345678")
        self.user.save()
        self.data = {"username": "testuser", "password": "ken12345678"}

        res = self.client.post("/users/login/", data=self.data, format="json")
        self.token = res.data["token"]
        self.headers = {
            "HTTP_AUTHORIZATION": self.token,
            "Content-Type": "application/json",
        }
