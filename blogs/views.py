from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post-new.html"
    fields = ['title', 'body', 'author']
    success_url = '/'  # Redirect to home page after successful creation

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post-update.html"
    fields = ['title', 'body']
    success_url = '/'  # Redirect to home page after successful update