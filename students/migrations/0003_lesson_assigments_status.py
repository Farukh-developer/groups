# Generated by Django 5.0.6 on 2024-06-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_lesson_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='assigments_status',
            field=models.BooleanField(default=True),
        ),
    ]