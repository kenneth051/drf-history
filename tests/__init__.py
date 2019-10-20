from django.test import TestCase, Client

from django.contrib.auth.models import User


class BaseTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="testuser")
        self.user.set_password("12345")
        self.user.save()
