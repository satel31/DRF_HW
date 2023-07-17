from rest_framework import serializers

from apps.courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
