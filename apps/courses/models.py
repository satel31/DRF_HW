from django.db import models

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

    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
