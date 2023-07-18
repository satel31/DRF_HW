from django.core.management import BaseCommand
from apps.courses.models import Course, Lesson, Payment
from apps.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # users
        pip = User.objects.get(email='pip@mail.ru')
        aragorn = User.objects.get(email='AragornTheKing@mail.ru')
        melko = User.objects.get(email='melko@mail.ru')

        # course
        cj = Course.objects.get(course_name='Criminal Justice')
        cl = Course.objects.get(course_name='Civil Law')
        ss = Course.objects.get(course_name='Soft skills of the Lawyer')

        # lesson
        clgp = Lesson.objects.get(lesson_name='Civil Law (general part)')
        pil = Lesson.objects.get(lesson_name='Public International Law')
        eng = Lesson.objects.get(lesson_name='English for a Lawyer')

        payment_list = [
            {'user': pip, 'course': cj, 'sum': 10_000, 'method': 'cash'},
            {'user': pip, 'lesson': clgp, 'sum': 2_000, 'method': 'cash'},

            {'user': aragorn, 'course': cl, 'sum': 8_000, 'method': 'card'},
            {'user': aragorn, 'course': ss, 'sum': 5_000, 'method': 'card'},
            {'user': aragorn, 'lesson': pil, 'sum': 3_000, 'method': 'card'},

            {'user': melko, 'lesson': eng, 'sum': 4_000, 'method': 'card'},
        ]

        Payment.objects.all().delete()

        payments_to_create = []

        for payment in payment_list:
            payments_to_create.append(Payment(**payment))

        Payment.objects.bulk_create(payments_to_create)
