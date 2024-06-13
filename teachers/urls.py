from django.urls import path
from .views import TeacherDashboardView, TeacherTeamView, StudentByTeamView, TeacherHomeworkView, StudentGroupView

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('groups/', TeacherTeamView.as_view(), name='groups'),
    path('lesson/<int:id>/', StudentByTeamView.as_view(), name='lessons'),
    path('homework/<int:id>/', TeacherHomeworkView.as_view(), name='homework'),
    path('students/<int:id>/', StudentGroupView.as_view(), name='students'),
    
    
    
   
]
