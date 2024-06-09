from django.db import models
from blog.models import Team, Student
# Create your models here.
class Lesson(models.Model):
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lessons')
    theme=models.CharField(max_length=150)
    date=models.DateField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    assigments_status=models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['team','theme']
    
    def __str__(self):
        return f'{self.theme}'
    
class Exercise(models.Model):
    lesson=models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='homework')
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    description=models.TextField()
    homework_file=models.FileField(upload_to='homework/', blank=True, null=True)
    date=models.DateField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ['student','lesson']
        
        
    def __str__(self):
        return f'{self.student.user_id.first_name}  {self.lesson.theme}'
    