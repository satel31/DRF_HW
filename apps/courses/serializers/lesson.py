from rest_framework import serializers

from apps.courses.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='course_name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
