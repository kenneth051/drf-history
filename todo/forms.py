from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    todo = forms.CharField(label="todo")

    class Meta:
        model = Todo
        fields = ["todo"]
