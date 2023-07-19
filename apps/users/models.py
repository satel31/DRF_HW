from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    city = models.CharField(max_length=235, verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    first_name = models.CharField(max_length=235, verbose_name='Name', **NULLABLE)
    last_name = models.CharField(max_length=235, verbose_name='Last name', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
