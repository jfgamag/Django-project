
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
    path('', posts_views.list_posts, name='feed'),
    path('posts/new/', posts_views.create_post, name='create_post'),
    path('users/', user_m.Profile, name='profile'),
    path('users/login', user_views.login_view, name='login'),
    path('users/logout', user_views.logout_view, name='logout'),
    path('users/signup', user_views.signup_view, name='signup'),
    path('users/me/profile', user_views.update_profile, name='update_profile'),
    
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
