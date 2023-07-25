from rest_framework.permissions import BasePermission

from apps.users.models import UserRoles


class IsOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class ModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE']:
            return request.user.role != UserRoles.MODERATOR
        return request.user.role == UserRoles.MODERATOR
