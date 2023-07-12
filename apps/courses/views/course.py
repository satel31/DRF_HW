from rest_framework.viewsets import ModelViewSet

from apps.courses.models import Course
from apps.courses.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
