from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_update_email(email_list, course):
    """Sends an email with update of the course"""
    try:
        send_mail(
            'Course update!',
            f'Course {course} has been updated. Check it out!',
            settings.EMAIL_HOST_USER,
            email_list
        )
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send. Error: {e}')
