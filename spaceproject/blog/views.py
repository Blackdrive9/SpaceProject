from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})
