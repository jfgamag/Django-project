#Posts views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Models
from posts.models import Post
# Forms
from posts.forms import PostForm

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name='posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset= Post.objects.all()


class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

@login_required
def create_post(request):
    """"Creates new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:feed')
    else:
        form = PostForm()

    return render(
            request, 
            template_name='posts/new.html', 
            context={
                    'form': form,
                    'user': request.user,
                    'profile': request.user.profile
            },
        )
