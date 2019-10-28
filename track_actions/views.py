from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from track_actions.serializers import HistorySerializer
from track_actions.models import History


class HistoryView(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    http_method_names = ["get"]
