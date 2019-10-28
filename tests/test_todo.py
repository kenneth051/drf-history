from tests import BaseTests
from track_actions.models import History
from app_test.models import Todo
from django.urls import reverse
import ast
from rest_framework.reverse import reverse


class TestTodo(BaseTests):
    def test_create_to_do_without_authentication(self):
        # create
        data = {"action": "write code"}
        response = self.client.post(
            reverse("todo-list"), HTTP_AUTHORIZATION=None, data=data
        )
        self.assertEqual(response.status_code, 403)

    def test_create_to_do_with_bad_authentication(self):
        data = {"action": "write code"}
        response = self.client.post(
            reverse("todo-list"), HTTP_AUTHORIZATION="None", data=data
        )
        self.assertEqual(response.status_code, 403)

    def test_create_update_delete_to_do_get_history(self):
        # create
        data = {"action": "write code"}
        response = self.client.post(
            reverse("todo-list"),
            HTTP_AUTHORIZATION=self.token,
            data=data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        # check for history
        history = History.objects.get(id=2)
        self.assertEquals(history.__dict__["action"], "POST")
        self.assertEquals(history.__dict__["table_name"], "app_test_todo")
        request_data = ast.literal_eval(history.__dict__["request_data"])
        self.assertEquals(request_data["action"], data["action"])

        # update
        data1 = {"action": "edit code"}
        edit_todo_url = reverse("todo-detail", args={response.data.get("id")})
        response = self.client.put(
            edit_todo_url,
            HTTP_AUTHORIZATION=self.token,
            data=data1,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        # check for history
        history = History.objects.get(id=3)
        self.assertEquals(history.__dict__["action"], "PUT")
        self.assertEquals(history.__dict__["table_name"], "app_test_todo")
        request_data = ast.literal_eval(history.__dict__["request_data"])
        self.assertEquals(request_data["action"], data1["action"])

        # # delete
        response = self.client.delete(
            edit_todo_url,
            HTTP_AUTHORIZATION=self.token,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 204)
        # check for delete history
        history = History.objects.get(id=4)
        self.assertEquals(history.__dict__["action"], "DELETE")
        self.assertEquals(history.__dict__["table_name"], "app_test_todo")
