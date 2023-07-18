from django.core.management import BaseCommand
from apps.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_list = [
            {'email': 'pip@mail.ru', 'phone': '+1 111 111 1111', 'city': 'Shire', 'avatar': ''},
            {'email': 'AragornTheKing@mail.ru', 'phone': '+2 222 222 2222', 'city': 'Minas Tirith', 'avatar': ''},
            {'email': 'melko@mail.ru', 'phone': '+0 000 000 0000', 'city': 'Angband', 'avatar': ''},
        ]

        User.objects.all().delete()

        users_to_create = []

        for user in user_list:
            users_to_create.append(User(**user))

        User.objects.bulk_create(users_to_create)
