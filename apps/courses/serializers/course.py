from rest_framework import serializers

from apps.courses.models import Course, Lesson, Subscription
from apps.courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)
    subscription = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course.pk).count()

    def get_subscription(self, course):
        return Subscription.objects.filter(course=course).exists()

    class Meta:
        model = Course
        fields = ('course_name', 'preview', 'description', 'lesson_count', 'lesson', 'subscription',)
