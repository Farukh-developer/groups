# Generated by Django 5.0.6 on 2024-06-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_student_teacher_alter_user_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('student', 'student'), ('admin', 'admin'), ('teacher', 'teacher')], default='student', max_length=10),
        ),
    ]
