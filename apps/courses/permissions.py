from rest_framework.permissions import BasePermission

from apps.users.models import UserRoles


class IsNotModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.role != UserRoles.MODERATOR
