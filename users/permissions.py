from .models import User
from rest_framework import permissions
from rest_framework.views import View
import jwt
import ipdb


class IsAuthenticatedAndAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class IsActiveTrue(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_authenticated and request.user.isActive


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_superuser
