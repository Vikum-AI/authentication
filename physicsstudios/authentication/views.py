from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model


from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
