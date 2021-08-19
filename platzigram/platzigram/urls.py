
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from posts import views as posts_views
from users import models as user_m


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('posts/', posts_views.list_posts),
    path('users/', user_m.Profile),
    
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
