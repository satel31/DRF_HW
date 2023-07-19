from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.permissions import IsOwnerPermission
from apps.users.serializers import UserSerializer, StrangerUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    default_permission_class = [IsAuthenticated()]
    permissions = {
        'create': [AllowAny()],
        'update': [IsAuthenticated(), IsOwnerPermission()],
        'partial_update': [IsAuthenticated(), IsOwnerPermission()],
        'destroy': [IsAuthenticated(), IsOwnerPermission()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission_class)

    def get_serializer_class(self):
        try:
            if self.request.user.email == self.get_object().email:
                return UserSerializer
            return StrangerUserSerializer
        # игнорирование ошибки при list
        except AssertionError:
            return StrangerUserSerializer
