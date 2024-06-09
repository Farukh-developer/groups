from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm, StudentForm, TeamForm, StudentEditForm, ResetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Student, Team
from .permission import AdminRequiredMixin
from django.db.models import Q

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')

        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})


class RegisterView(AdminRequiredMixin,View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if user.user_role == 'student':
                new_student= Student()
                new_student.user_id = user
                new_student.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'user/profile.html')

class EditProfileView(LoginRequiredMixin,View):
    def get(self, request, id):
        profile=User.objects.get(id=id)
        form=ProfileEditForm(instance=request.user)
        return render(request, 'user/edit.html', context={"form":form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/') 
        return render(request, 'user/edit.html', {'form': form})
        
class GroupsView(View):
    def get(self, request):
        team =Team.objects.all()
        return render(request, 'user/group.html', context={"team": team})
 
def read(request, id):
    team=Team.objects.get(id=id)
    return render(request, 'user/read.html', context={"team":team})
    
def create(request):
    form=TeamForm()
    if request.method=='POST':
        form=TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'user/create.html', context={"form":form})   

def update(request, id):
    team=get_object_or_404(Team, id=id)
    form=TeamForm(instance=team)
    if request.method=='POST':
        form=TeamForm(request.POST,request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('users:group')
    return render(request, 'user/create.html', context={"form":form})  


def delete(request, id):
    team=get_object_or_404(Team, id=id)
    team.delete()
    return redirect('users:group')  



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")
    
    
    
class StudentsListView(AdminRequiredMixin, View):
    def get(self, request):
        if request.GET != {}:
            students=Student.objects.filter(Q(user_id__username__icontains=request.GET['search']))
        else:    
          students=Student.objects.all()
        return render(request, 'user/students.html', context={"students":students})
    
    
class StudentByTeamView(AdminRequiredMixin, View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        students=team.students.all()
        return render(request, 'user/students.html', context={"students":students})      
    
    
class EditStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student=get_object_or_404(Student, id=id)
        form=StudentEditForm(instance=student)
        return render(request, 'user/edit_student.html', context={"form":form})
    
    
    def post(self, request, id):
        student=get_object_or_404(Student, id=id)
        form=StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:students')
        form=StudentEditForm(instance=student)
        return render(request, 'user/edit_student.html', context={"form":form})
    
            
class DeleteStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student=get_object_or_404(Student, id=id)
        user=User.objects.get(username=student.user_id.username)
        student.delete()
        user.delete()
        return redirect('users:students')
           
     

    
    
class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm
        return render(request, 'user/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('/')
        form = ResetPasswordForm
        return render(request, 'user/reset_password.html', {'form':form})

    