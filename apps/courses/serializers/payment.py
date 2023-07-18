from rest_framework import serializers

from apps.courses.models import Payment, Course, Lesson


class PaymentSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='course_name', queryset=Course.objects.all())
    lesson = serializers.SlugRelatedField(slug_field='lesson_name', queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
