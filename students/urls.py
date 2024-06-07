from django.urls import path

from .views import StudentDashboardView, StudentGroupView
app_name = 'students'

urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('groups/', StudentGroupView.as_view(), name='groups'),
    
]
