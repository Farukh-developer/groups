from django.urls import path
from .views import LoginView, RegisterView, ProfileView, EditProfileView, create, GroupsView, delete, LogoutView, read, update

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
   
    path('group/', GroupsView.as_view(), name='group'),
    path('create/', create, name='create'),

    path('read/<int:id>/', read, name='read'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),

##########
#    path('', LoginView.as_view(), name='login'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('logout/', LogautView.as_view(), name='logout'),
#     path('create/', Create.as_view(), name='create'),
#     path('profil/<int:id>/', ProfileView.as_view(), name='profil'),
#     path('edit/<int:id>/', EditProfileView.as_view(), name='edit'),
#     path('delete/<int:id>/', delete, name='delete'),
#     path('students/', TableView.as_view(), name='students'),
    
    
    
    
    
]