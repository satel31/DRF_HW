from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.courses.models import Course, Subscription, Lesson
from apps.courses.pagination import CoursePagination
from apps.courses.permissions import ModeratorPermission, IsOwnerPermission
from apps.courses.serializers.course import CourseSerializer
from apps.courses.tasks import send_update_email
from apps.users.models import UserRoles, User
import datetime


class CourseViewSet(ModelViewSet):
    """Viewset for Course model.
       To create you need to enter course_name.
       Has pagination for GET method and different permissions for different methods.
       In queryset has only owner's objects"""
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    # In case of test
    #permission_classes = [AllowAny]
    default_permission_class = [IsAuthenticated()]
    permissions = {
        'create': [IsAuthenticated(), ModeratorPermission()],
        'list': [IsAuthenticated() or ModeratorPermission()],
        'retrieve': [IsAuthenticated() or ModeratorPermission()],
        'update': [IsAuthenticated(), IsOwnerPermission() or ModeratorPermission()],
        'partial_update': [IsAuthenticated(), IsOwnerPermission() or ModeratorPermission()],
        'destroy': [IsAuthenticated(), ModeratorPermission(), IsOwnerPermission()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission_class)


    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        upd_course = serializer.save()
        send_update_email.delay(upd_course.pk)


    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)
