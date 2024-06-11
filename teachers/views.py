from django.shortcuts import render, get_object_or_404
from django.views import View
from blog.permission import TeacherRequiredMixin
from blog.models import Teacher, Team


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')
    
    
class TeacherTeamView(TeacherRequiredMixin, View):
    def get(self, request):
        teacher=get_object_or_404(Teacher, user=request.user)
        teams=teacher.teams.all()
        return render(request, 'teacher/groups.html', context={"teams":teams})
    
    


class StudentByTeamView(TeacherRequiredMixin, View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        lessons=team.lessons.all()
        return render(request, 'teacher/lessons.html', context={"lessons":lessons})  
    

class Students(TeacherRequiredMixin, View):
    def get(self, request):
        team = get_object_or_404(Teacher, user=request.user)
        students=team.students.all()
        return render(request, 'teacher/students.html', context={"students":students})
    