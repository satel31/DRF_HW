from rest_framework import serializers

from apps.courses.models import Course, Lesson
from apps.courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course.pk).count()

    class Meta:
        model = Course
        fields = ('course_name', 'preview', 'description', 'lesson_count', 'lesson',)


#class CourseListSerializer(serializers.ModelSerializer):
    #lesson_count = serializers.SerializerMethodField()

    #def get_lesson_count(self, course):
        #return Lesson.objects.filter(course=course.pk).count()

    #class Meta:
        #model = Course
        #fields = ('course_name', 'lesson_count', 'preview',)


#class CourseDetailSerializer(serializers.ModelSerializer):
    #lessons = serializers.SerializerMethodField()

    #def get_lessons(self, course):
        #return [lesson.lesson_name for lesson in Lesson.objects.filter(course=course.pk)]

    #class Meta:
        #model = Course
        #fields = ('course_name', 'lessons', 'preview', 'description',)
