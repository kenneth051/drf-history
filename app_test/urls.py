# Third-Party Imports
from django.conf.urls import include
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from app_test.views import LoginView, TodoView
from track_actions import urls

router = SimpleRouter()
router.register("todo", TodoView, "todo")
urlpatterns = [
    path("users/login/", LoginView.as_view()),
    path("track_actions/", include(urls)),
]

urlpatterns += router.urls
