from rest_framework import serializers

from apps.courses.models import Subscription, Course
from apps.courses.services import get_pay_link


class SubscriptionSerializer(serializers.ModelSerializer):
    payment_link = serializers.SerializerMethodField()

    def get_payment_link(self, instance):
        obj = Course.objects.get(pk=instance.course.pk)
        return get_pay_link(obj)

    class Meta:
        model = Subscription
        fields = '__all__'
