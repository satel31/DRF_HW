from rest_framework import serializers

from apps.courses.models import Payment
from apps.users.models import User

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    def get_payments(self, user):
        return Payment.objects.filter(user=user.pk).values()

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'city', 'avatar', 'phone', 'payments', 'password')

class StrangerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'city', 'avatar', 'phone',)
