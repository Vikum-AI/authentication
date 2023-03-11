from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response


from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
