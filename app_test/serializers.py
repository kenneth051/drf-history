from rest_framework import serializers
from app_test.models import Todo
from django.contrib.auth import authenticate
from app_test.utils import token


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.ReadOnlyField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("username or Password is incorrect")
        user_token = token(user)
        return {"username": user.username, "token": user_token}


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("user", "id", "action", "created_at")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        data = super().create(validated_data)
        return data
