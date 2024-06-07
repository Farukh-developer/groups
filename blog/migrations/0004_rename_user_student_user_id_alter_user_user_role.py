# Generated by Django 5.0.6 on 2024-06-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_user_id_student_user_alter_user_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('admin', 'admin')], default='student', max_length=10),
        ),
    ]