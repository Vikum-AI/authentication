from rest_framework import serializers
from django.contrib.auth import get_user_model
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
