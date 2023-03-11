from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.exceptions import AuthenticationFailed

from .models import MyUser

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name',
                  'email', 'password', 'roles']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            roles=validated_data['roles']
        )

        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=256, source='username')
    password = serializers.CharField(
        max_length=65, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'password', 'tokens']

    def get_tokens(self, obj):
        return obj

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': f"{refresh}",
            'access': f"{refresh.access_token}"
        }

    def validate(self, attrs):
        param_email = attrs.get('username', "")
        param_password = attrs.get('password', "")

        user = authenticate(username=param_email, password=param_password)

        if User.objects.filter(username=param_email, is_active=False).exists():
            raise AuthenticationFailed("Account disabled")

        if not user:
            raise AuthenticationFailed("Invalid credentials, try again.")

        tokens = self.get_tokens_for_user(user)

        return {
            'username': param_email,
            'access_token': tokens['access'],
            'refresh_token': tokens['refresh']
        }
