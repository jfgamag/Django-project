"""User admin classes
"""
from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    """Profile admin
    """
    pass