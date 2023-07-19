from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.courses.models import Course
from apps.courses.permissions import IsNotModerator
from apps.courses.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    default_permission_class = [IsAuthenticated()]
    permissions = {
        'create': [IsAuthenticated(), IsNotModerator()],
        'destroy': [IsAuthenticated(), IsNotModerator()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission_class)

