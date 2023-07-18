from django.db import models

from apps.users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_name = models.CharField(max_length=235, verbose_name='Course name')
    preview = models.ImageField(upload_to='courses/', verbose_name='Course preview', **NULLABLE)
    description = models.TextField(verbose_name='Course description', **NULLABLE)

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=235, verbose_name='Lesson name')
    description = models.TextField(verbose_name='Lesson description', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/', verbose_name='Lesson preview', **NULLABLE)
    video_link = models.URLField(max_length=235, verbose_name='Video link', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Course', **NULLABLE)

    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

class Payment(models.Model):
    METHOD_CHOICES = (
        ('cash', 'cash'),
        ('card', 'card'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='Paid Course', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Paid Lesson', **NULLABLE)
    sum = models.IntegerField(default=0, verbose_name='Sum of Payment')
    method = models.CharField(max_length=255, choices=METHOD_CHOICES, verbose_name='Payment Method')
