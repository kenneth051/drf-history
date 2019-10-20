from tests import BaseTests
from track_actions.models import History
from todo.models import Todo
from django.urls import reverse
import ast

class TestTodo(BaseTests):
    def test_create_todo(self):
        login = self.client.login(username='testuser', password='12345')
        data={'todo': 'run tests'}
        response = self.client.post('/todo/', data)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<form')
        self.assertContains(response, 'run tests')
        
        #check for history
        history=History.objects.get(id=1)
        self.assertEquals(history.__dict__["action"], "POST")
        self.assertEquals(history.__dict__["table_name"], "todo_todo")
        response_data=ast.literal_eval(history.__dict__["response_data"])
        self.assertEquals(response_data["todo"], data["todo"])
    
    def test_delete_todo_gets_recorded_in_history_model(self):
        login = self.client.login(username='testuser', password='12345')
        data={'todo': 'work out'}
        response = self.client.post('/todo/', data)
        response = self.client.delete(reverse('delete',args=(1,)))
        
        #check for delete history
        history=History.objects.get(id=2)
        self.assertEquals(history.__dict__["action"], "DELETE")
        self.assertEquals(history.__dict__["table_name"], "todo_todo")
        response_data=ast.literal_eval(history.__dict__["response_data"])
        self.assertEquals(response_data["todo"], data["todo"])


        