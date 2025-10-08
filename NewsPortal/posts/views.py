from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    """Список всех новостей"""
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

class PostDetail(DetailView):
    """Отдельная новость"""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'