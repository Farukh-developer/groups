from django.shortcuts import render

# Create your views here.
from blog.permission import StudentRequiredMixin
from django.views import View
from blog.models import Student
class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')
    
class StudentGroupView(StudentRequiredMixin, View):
    def get(self, request):
        student=Student.objects.get(user_id=request.user)
        return render(request, 'students/groups.html', context={"student":student})