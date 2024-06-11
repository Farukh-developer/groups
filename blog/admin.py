from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Student, Team, Teacher
# Register your models here.
admin.site.register([User, Student, Team, Teacher])
