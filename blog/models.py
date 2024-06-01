

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE_CHOICES = {
        ("student", "student"),
        ("teacher", "teacher"),
        ("admin", "admin"),
    }
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default="profile_pics/default.jpeg")
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default="student")



class Team(models.Model):
    name=models.CharField(max_length=70, unique=True)
    date_created=models.DateField(auto_now_add=True)
    end_date=models.DateField(blank=True, null=True)
    

class Student(models.Model):
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    