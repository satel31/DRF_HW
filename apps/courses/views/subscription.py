from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.courses.models import Subscription
from apps.courses.serializers.subscription import SubscriptionSerializer
from apps.users.models import UserRoles


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    #permission_classes = [IsAuthenticated]
    # In case of test
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.user = self.request.user
        new_sub.save()

class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    # In case of test
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Subscription.objects.all()
        return Subscription.objects.filter(user=self.request.user)
