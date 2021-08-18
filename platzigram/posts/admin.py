#Django
from django.contrib import admin
# from django.contrib.auth.models import User
#models
from posts.models import Post

# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    """Post admin class"""
    list_display = ('pk','user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    search_fields = (
        'title',
        'pk',
        'user__username'
    )

    fieldsets = (
        ('Posts', {
            'fields': (
                ('user', 'title'),)
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),)
        }),
    )
    readonly_fields = ('created', 'modified')

    