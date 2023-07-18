from rest_framework import serializers

from apps.courses.models import Payment
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    def get_payments(self, user):
        return Payment.objects.filter(user=user.pk).values()

    class Meta:
        model = User
        fields = ('email', 'city', 'avatar', 'phone', 'payments',)
