from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile 


admin.site.register(Profile)