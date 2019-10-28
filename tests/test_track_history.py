from tests import BaseTests
from track_actions.models import History
from django.urls import reverse
from rest_framework.reverse import reverse


class TestViewHistory(BaseTests):
    def test_get_history(self):
        data = {"action": "sleep"}
        response = self.client.post(
            reverse("todo-list"),
            HTTP_AUTHORIZATION=self.token,
            data=data,
            content_type="application/json",
        )
        data = {"action": "wake up"}
        response = self.client.post(
            reverse("todo-list"),
            HTTP_AUTHORIZATION=self.token,
            data=data,
            content_type="application/json",
        )
        response = self.client.get(
            reverse("history-list"), HTTP_AUTHORIZATION=self.token
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], History.objects.count())
