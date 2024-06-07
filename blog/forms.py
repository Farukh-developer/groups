from django import forms
from .models import User, Student, Team


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password
    
class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    class Meta:
        model=User
        fields=('username', 'phone_number', 'first_name', 'last_name')
  
  
  
  
class StudentForm(forms.ModelForm):
    user_id = forms.CharField(widget=forms.NumberInput({"class": "form-control", "placeholder": "id"}))
    date_of_birth= forms.DateField(widget=forms.DateInput({"class": "form-control", "placeholder": "Birth date"}))
    end_date = forms.DateField(widget=forms.DateInput({"class": "form-control", "placeholder": "date",}))
    team= forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Enter Team name", }))

   
    class Meta:
        model = Student
        fields = ('user_id', 'date_of_birth', 'end_date', 'team')
        
        
        
  
class TeamForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "name"}))
    end_date = forms.DateField(widget=forms.DateInput({"class": "form-control", "placeholder": "date",}))
   
   
    class Meta:
        model = Team
        fields = ('name', 'end_date')
            



class StudentEditForm(forms. ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput({"class": "form-control"}))



    
    class Meta:
        model = Student
        fields = ('date_of_birth', 'team')