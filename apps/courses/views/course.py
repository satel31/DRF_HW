from rest_framework.viewsets import ModelViewSet

from apps.courses.models import Course
from apps.courses.serializers.course import CourseSerializer
#, CourseListSerializer, CourseDetailSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #default_serializer = CourseSerializer
    #serializers = {
        #'list': CourseListSerializer,
        #'retrieve': CourseDetailSerializer,
    #}

    #def get_serializer_class(self):
        #return self.serializers.get(self.action, self.default_serializer)
