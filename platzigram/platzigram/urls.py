
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from posts import views as posts_views
from users import views as user_views
from platzigram import views as local_views
from users import models as user_m


urlpatterns = [ 
    path('admin/', admin.site.urls, name='hello_world'),
    path('sort/', local_views.sort_n, name='sort'),
    path('hi/', local_views.hello, name='hi'),
    path('posts/', posts_views.list_posts, name='feed'),
    path('users/', user_m.Profile, name='profile'),
    path('users/login', user_views.login_view, name='login'),
    
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
