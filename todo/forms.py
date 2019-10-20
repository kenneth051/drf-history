from django import forms
from django.contrib.auth import authenticate, get_user_model
from todo.models import Todo

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            return super().clean(*args, **kwargs)
        
class UserRegisterForm(forms.ModelForm):
    email=forms.EmailField(label="Email Field")
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=get_user_model()
        fields=[
            "username",
            "email",
            "password"
        ]

class TodoForm(forms.ModelForm):
    todo=forms.CharField(label="todo")
    class Meta:
        model=Todo
        fields=[
            "todo"
        ]
    
            
        