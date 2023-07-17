from django.core.management import BaseCommand
from apps.courses.models import Course


class Command(BaseCommand):
    def handle(self, *args, **options):
        course_list = [
            {'course_name': 'Criminal Justice', 'preview': '',
             'description': 'This course considers all aspects of the criminal justice process'},
            {'course_name': 'Civil Law', 'preview': '',
             'description': 'This course considers all aspects of the civil law'},
            {'course_name': 'Soft skills of the Lawyer', 'preview': '',
             'description': 'Study the most important soft skills'},
            {'course_name': 'International Law', 'preview': '',
             'description': 'This course considers all aspects of the international law'},
        ]

        Course.objects.all().delete()

        courses_to_create = []

        for course in course_list:
            courses_to_create.append(Course(**course))

        Course.objects.bulk_create(courses_to_create)
