"""User admin classes
"""
from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin
    """
    list_display = ('user', 'website', 'phone_number', 'picture')

