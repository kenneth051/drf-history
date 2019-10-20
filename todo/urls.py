from django.urls import path, include
from todo.views import todoView, deleteView

urlpatterns = [
    path("delete/<str:id>/", deleteView, name="delete"),
    path("todo/", todoView, name="todo"),
]
