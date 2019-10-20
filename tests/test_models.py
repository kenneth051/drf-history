from tests import BaseTests
from track_actions.models import History
from todo.models import Todo
from django.urls import reverse


class TestHistoryModel(BaseTests):
    def test_history_model(self):
        count = 0

        history = History(
            table_name="our model table",
            user=self.user,
            instance_id="1",
            action="POST",
            request_data="request data}",
            response_data="{response data}",
        )
        history.save()

        self.assertEquals(History.objects.count(), count + 1)

    def test_todo_model(self):
        count = 0
        todo = Todo(todo="test app", user=self.user)
        todo.save()
        self.assertEquals(Todo.objects.count(), count + 1)
