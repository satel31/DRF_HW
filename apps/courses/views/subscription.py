from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.courses.models import Subscription
from apps.courses.serializers.subscription import SubscriptionSerializer
from apps.users.models import UserRoles


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """View to create a subscription.
       To create you need to enter course pk (from existed courses) and method (cash or card).
       In case of the tests don't forget to change permissions."""
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    # In case of test
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.user = self.request.user
        new_sub.save()

class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    """View to delete a subscription by its id (you can delete only your own subscription).
       In case of the tests don't forget to change permissions."""
    permission_classes = [IsAuthenticated]
    # In case of test
    #permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Subscription.objects.all()
        return Subscription.objects.filter(user=self.request.user)
