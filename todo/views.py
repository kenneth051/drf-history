from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import TodoForm
from .models import Todo


def deleteView(request, id):
    Todo.objects.filter(id=id).delete()
    return redirect("/todo/todo")


@login_required
def todoView(request):
    form = TodoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
    user_todo = Todo.objects.filter(user=request.user)
    form = TodoForm()
    context = {"form": form, "todos": user_todo, "delete": deleteView}
    return render(request, "todo.html", context)
