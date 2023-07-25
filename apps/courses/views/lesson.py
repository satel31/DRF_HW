from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Lesson
from apps.courses.permissions import ModeratorPermission, IsOwnerPermission
from apps.courses.serializers.lesson import LessonSerializer
from apps.users.models import UserRoles


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated or ModeratorPermission]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | ModeratorPermission]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission | IsOwnerPermission]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermission, IsOwnerPermission]

    def get_queryset(self):
        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)
