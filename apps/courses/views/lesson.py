import datetime

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.courses.models import Lesson, Course, Subscription
from apps.courses.pagination import LessonPagination
from apps.courses.permissions import ModeratorPermission, IsOwnerPermission
from apps.courses.serializers.lesson import LessonSerializer
from apps.users.models import UserRoles, User
from apps.courses.tasks import send_update_email
import datetime


class LessonCreateAPIView(generics.CreateAPIView):
    """View to create a lesson.
       To create you need to enter lesson_name and course_name (from existed courses).
       In case of the tests don't forget to change permissions."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]
    # In case of test
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """View to get a list of lessons (returns only your own lessons).
       Has pagination.
       In case of the tests don't forget to change permissions."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated or ModeratorPermission]
    # In case of test
    #permission_classes = [AllowAny]
    pagination_class = LessonPagination

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDetailAPIView(generics.RetrieveAPIView):
    """View to get a particular lesson by its id (returns only your own lessons).
       In case of the tests don't forget to change permissions."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | ModeratorPermission]
    # In case of test
    #permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)



class LessonUpdateAPIView(generics.UpdateAPIView):
    """View to update a lesson by its id (you can update only your own lessons).
       In case of the tests don't forget to change permissions."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission | IsOwnerPermission]
    # In case of test
    #permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        upd_lesson = serializer.save()
        course = Course.objects.filter(pk=upd_lesson.course_id).first()
        send_update_email.delay(course.pk)

class LessonDeleteAPIView(generics.DestroyAPIView):
    """View to delete a lesson by its id (you can delete only your own lessons).
       In case of the tests don't forget to change permissions."""
    permission_classes = [IsAuthenticated, ModeratorPermission, IsOwnerPermission]
    # In case of test
    #permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)
