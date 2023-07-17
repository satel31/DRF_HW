from django.core.management import BaseCommand
from apps.courses.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        cj = Course.objects.get(course_name='Criminal Justice')
        cl = Course.objects.get(course_name='Civil Law')
        ss = Course.objects.get(course_name='Soft skills of the Lawyer')
        il = Course.objects.get(course_name='International Law')

        lesson_list = [
            {'lesson_name': 'Criminal Law', 'description': 'Criminal Law lessons', 'preview': '', 'video_link': '',
             'course': cj},
            {'lesson_name': 'Criminal Procedure', 'description': 'Criminal Procedure lessons', 'preview': '',
             'video_link': '', 'course': cj},
            {'lesson_name': 'Criminology', 'description': 'Criminology lessons', 'preview': '',
             'video_link': '', 'course': cj},
            {'lesson_name': 'Forensic Science', 'description': 'Forensic Science lessons', 'preview': '',
             'video_link': '', 'course': cj},

            {'lesson_name': 'Civil Law (general part)', 'description': 'Civil Law lessons (general part)',
             'preview': '', 'video_link': '', 'course': cl},
            {'lesson_name': 'Civil Law (special part)', 'description': 'Civil Law lessons (special part)',
             'preview': '', 'video_link': '', 'course': cl},

            {'lesson_name': 'Oratory of a Lawyer', 'description': 'Oratory of a Lawyer lessons',
             'preview': '', 'video_link': '', 'course': ss},
            {'lesson_name': 'English for a Lawyer', 'description': 'English for a Lawyer lessons',
             'preview': '', 'video_link': '', 'course': ss},
            {'lesson_name': 'Latin for a Lawyer', 'description': 'Latin for a Lawyer lessons',
             'preview': '', 'video_link': '', 'course': ss},

            {'lesson_name': 'Public International Law', 'description': 'Public International Law lessons',
             'preview': '', 'video_link': '', 'course': il},
            {'lesson_name': 'Private International Law', 'description': 'Private International Law lessons',
             'preview': '', 'video_link': '', 'course': il},
        ]

        Lesson.objects.all().delete()

        lessons_to_create = []

        for lesson in lesson_list:
            lessons_to_create.append(Lesson(**lesson))

        Lesson.objects.bulk_create(lessons_to_create)
