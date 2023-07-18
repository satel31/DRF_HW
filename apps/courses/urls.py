from django.urls import path
from rest_framework.routers import SimpleRouter
from apps.courses.views.lesson import *

from apps.courses.views.course import CourseViewSet
from apps.courses.views.payment import *

app_name = 'courses'

urlpatterns = [
    # lesson
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('add_lesson/', LessonCreateAPIView.as_view(), name='add_lesson'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

    # payment
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
    path('payment/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment'),
]

router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns += router.urls
