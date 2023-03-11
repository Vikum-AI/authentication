from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .managers import CustomUserManager
from datetime import datetime
from uuid import uuid4
# Create your models here.


class MyUser(AbstractUser, PermissionsMixin):
    # CUSTOM ROLES FOR DEVELOPMENT
    DEV = 1
    ADMIN = 2

    # APP ROLES
    TEACHER = 3
    ASSISTANT = 4
    STUDENT = 5

    ROLE_CHOICES = (
        (DEV, 'dev'),
        (ADMIN, 'admin'),
        (TEACHER, 'teacher'),
        (ASSISTANT, 'assistant'),
        (STUDENT, 'student')
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    roles = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=False)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_date = models.DateTimeField(default=datetime.now())
    modified_date = models.DateTimeField(default=datetime.now())

    created_by = models.EmailField()
    modified_by = models.EmailField()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
