from django.views.generic import ListView,DetailView
from django.shortcuts import render
from .models import Post

class PostList(ListView):
    model = Post
    template_name= 'blog/blog.html'
    ordering= '-pk'

class PostDetail(DetailView):
    model = Post
    template_name='blog/blog_details.html'