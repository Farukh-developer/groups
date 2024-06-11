from django.urls import path
from .views import TeacherDashboardView, TeacherTeamView, StudentByTeamView

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('groups/', TeacherTeamView.as_view(), name='groups'),
    path('lesson/<int:group_id>/', StudentByTeamView.as_view(), name='lesson'),

    
   
]
