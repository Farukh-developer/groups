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
        return render(request, 'teacher/lessons.html', context={"lessons":lessons, "team":team})  
    

    
class TeacherHomeworkView(TeacherRequiredMixin, View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        lessons=team.homework.all()
        return render(request, 'teacher/lessons.html', context={"lessons":lessons, "team":team})  



class StudentGroupView(TeacherRequiredMixin, View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        students=team.students.all()
        return render(request, 'teachers/students.html', context={"students":students})
    

    

    