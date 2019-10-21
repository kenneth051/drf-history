from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo


def deleteView(request, id):
    """function to delete a specific todo
   
    Arguments:
       request {request object} -- request object in session
       id {integer} -- Todo object Id to delete
   
    Returns:
       redirects to todo page to show the remaining Todos
    """
    Todo.objects.filter(id=id).delete()
    return redirect("/todo/todo")


@login_required
def todoView(request):
    """Todo view function to create and retrive all todos for a user
    
    Arguments:
        request {request object} -- request object in progress
    
    Returns:
        todo html page with rendered content
    """
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
