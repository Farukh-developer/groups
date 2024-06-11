from django.urls import path
from .views import TeacherDashboardView, TeacherTeamView, StudentByTeamView, Students

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('groups/', TeacherTeamView.as_view(), name='groups'),
    path('lesson/<int:id>/', StudentByTeamView.as_view(), name='lessons'),
    path('students/', Students.as_view(), name='students'),

    
   
]
