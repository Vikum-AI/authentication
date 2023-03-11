from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, first_name, last_name, roles, **kwargs):
        if not email:
            raise ValueError('Users must have at least one email address')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=email,
            roles=roles,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_deleted=False,
            is_staff=False,
            created_date=timezone.now(),
            modified_date=timezone.now(),
            created_by=email,
            modified_by=email,
            ** kwargs
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('User must have is_staff=True to be a superuser')
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'User must have is_superuser=True to be a superuser')
        return self.create_user(email=email, password=password, **kwargs)
