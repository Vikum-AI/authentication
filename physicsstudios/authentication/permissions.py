from rest_framework.permissions import BasePermission

# Dev and Admin
admin_roles = [1, 2]

# Teacher and assistant
teacher_roles = [3, 4]


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles in admin_roles)


class IsDev(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles == 1)


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles in teacher_roles)


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles == 5)
