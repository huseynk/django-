from django.contrib import admin
from django.db import models
from .forms import CustomUserChangeForms, CustomUserCreationForms
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForms
    form = CustomUserChangeForms
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',),}),)
        
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',),}),)

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
