from rest_framework import serializers

from apps.courses.models import Subscription, Course
from apps.courses.services import get_pay_link, create_payment_object


class SubscriptionSerializer(serializers.ModelSerializer):
    payment_link = serializers.SerializerMethodField()

    def get_payment_link(self, instance):
        obj = Course.objects.get(pk=instance.course.pk)
        payment_data = get_pay_link(obj)
        create_payment_object(instance, payment_data)
        return payment_data['url']

    class Meta:
        model = Subscription
        fields = '__all__'
