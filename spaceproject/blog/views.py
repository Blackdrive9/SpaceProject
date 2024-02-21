from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)
