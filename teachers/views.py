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
    
    
# class LessonView(TeacherRequiredMixin, View):
#     def get(self, request, group_id):
#         team = get_object_or_404(Team, id=group_id)
#         lessons = team.lessens.all()
#         return render(request, 'teacher/lesson.html', {'lessons': lessons})

class StudentByTeamView(TeacherRequiredMixin, View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        students=team.lessons.all()
        return render(request, 'teacher/lessons.html', context={"students":students})   