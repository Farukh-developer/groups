from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm, StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Student, Team
from .permission import AdminRequiredMixin
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
                return redirect('users:register')

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
                new_student.user = user
                new_student.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'user/profile.html')

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileEditForm(instance=user)
        return render(request, 'user/edit.html', {'form': form})

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


def delete(request, id):
    data = get_object_or_404(User, id=id)
    data.delete()
    return redirect("/")

   

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")
    
    
    
def read(request, id):
    student=Student.objects.get(id=id)
    return render(request, 'user/read.html', context={"student":student})

def create(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'user/create.html', context={"form":form})   


def update(request, id):
    student=get_object_or_404(Student, id=id)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'user/create.html', context={"form":form})  


def delete(request, id):
    student=get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users:profile')  
    
    