# Third-Party Imports
from django.urls import path
from rest_framework.routers import SimpleRouter
from track_actions.views import HistoryView

router = SimpleRouter()
router.register("history", HistoryView, "history")
urlpatterns = router.urls
