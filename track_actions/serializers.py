from rest_framework import serializers
from track_actions.models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = (
            "id",
            "table_name",
            "instance_id",
            "action",
            "user",
            "request_data",
            "response_data",
            "path",
            "created_at",
        )
