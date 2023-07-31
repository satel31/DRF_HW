# Generated by Django 4.2.3 on 2023-07-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_updated_at_alter_lesson_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time of update of materials of the course'),
        ),
    ]