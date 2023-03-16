from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .permissions import IsAdmin, IsTeacher, IsDev, IsStudent

User = get_user_model()


class RegisterStudentView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin | IsTeacher]


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class UserView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        user_info = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'roles': user.roles,
        }

        return Response(user_info)
