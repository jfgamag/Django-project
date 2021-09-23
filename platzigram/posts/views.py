#Posts views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
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
    paginate_by = 30
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy("posts:feed")

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['users'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
        
