import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from apps.courses.models import Subscription, Course, Lesson
from apps.users.models import User


@shared_task
def send_update_email(course_pk):
    """Sends an email with update of the course"""
    course = Course.objects.get(pk=course_pk)
    # Get all subscriptions by the course pk
    subscriptions = Subscription.objects.filter(course=course_pk)
    # Get all followers by user pk in subscriptions
    follower_list = User.objects.filter(pk__in=[subscription.user.pk for subscription in subscriptions])
    # Get all email by user pk in follower list
    email_list = [follower.email for follower in follower_list]

    current_time = timezone.now() - datetime.timedelta(minutes=1)

    if course.updated_at < current_time:
        try:
            send_mail(
                'Course update!',
                f'Course {course.course_name} has been updated. Check it out!',
                settings.EMAIL_HOST_USER,
                email_list
            )
            print('Email sent successfully')
        except Exception as e:
            print(f'Failed to send. Error: {e}')
    else:
        print(f'Course {course.course_name} was updated less than 4 hours ago')

    course.updated_at = current_time
    course.save()
