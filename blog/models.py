

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
    
    
    
class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date=models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username}"
   
    


class Team(models.Model):
    name=models.CharField(max_length=70, unique=True)
    date_created=models.DateField(auto_now_add=True)
    end_date=models.DateField(blank=True, null=True)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

    

class Student(models.Model):
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    def __str__(self):
        return f"{self.user_id.first_name}"

    