from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from app_test.serializers import LoginSerializer, TodoSerializer
from app_test.models import Todo


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
