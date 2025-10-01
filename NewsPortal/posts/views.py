from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    """Список всех новостей"""
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    """Отдельная новость"""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'