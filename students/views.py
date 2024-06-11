from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.permission import StudentRequiredMixin
from django.views import View
from blog.models import Student, Team
from students.models import Lesson, Exercise
from .forms import ExerciseForm


class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')
    
class StudentGroupView(StudentRequiredMixin, View):
    def get(self, request):
        student=Student.objects.get(user_id=request.user)
        return render(request, 'students/groups.html', context={"student":student})
    

class StudentLessonsView(StudentRequiredMixin, View):
    def get(self, request, group_id):
        team=get_object_or_404(Team, id=group_id)
        lessons=team.lessons.all()
        return render(request, 'students/lessons.html', context={"lessons":lessons})
    
    
class HomeworkView(StudentRequiredMixin, View):
    
    def get(self, request, lesson_id):
        form = ExerciseForm()
        return render(request, 'students/homework.html', context={"form": form})
    
    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        student = get_object_or_404(Student, user_id=request.user)
        
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            homework = Exercise()
            homework.lesson = lesson
            homework.student = student
            homework.description = form.cleaned_data['description']
            homework.homework_file = form.cleaned_data['homework_file']
            homework.save()
            
            lesson.assigments_status = True  
            lesson.save()
            return redirect('students:dashboard')

       
        return render(request, 'students/homework.html', context={"form": form})


class HomeWorkDetail(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        student=get_object_or_404(Student, user_id=request.user)
        lesson=get_object_or_404(Lesson, id=lesson_id)
        homework=Exercise.objects.filter(lesson=lesson, student=student).first()
        return render(request, 'students/home_detail.html', context={"homework":homework})
    

        

