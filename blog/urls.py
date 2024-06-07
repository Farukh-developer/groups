from django.urls import path
from .views import (LoginView, RegisterView, ProfileView, EditProfileView,  GroupsView, LogoutView, StudentsListView,
                    EditStudentView, DeleteStudentView, StudentByTeamView , delete, update, create, read)

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
   
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/int:id/', EditProfileView.as_view(), name='edit_profile'),
   
    
    path('group/', GroupsView.as_view(), name='group'),
    path('students', StudentsListView.as_view(), name='students'),
    path('edit-student/<int:id>/', EditStudentView.as_view(), name='edit_students'),
    path('delete-student/<int:id>/', DeleteStudentView.as_view(), name='delete_students'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/int:id/', EditProfileView.as_view(), name='edit_profile'),
    
    path('get-team-by-students/<int:id>/', StudentByTeamView.as_view(), name='team-students'),
    
    
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('read/<int:id>/', read, name='read'),
   
    
    

   
    
]