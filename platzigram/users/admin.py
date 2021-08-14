"""User admin classes
"""
from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin
    """
    # Display fields
    list_display = ('pk','user', 'website', 'phone_number', 'picture')
    # Display links that show user details
    list_display_links = ('pk','user')
    #Editable fields in django admin
    list_editable = ('phone_number', 'website', 'picture')
