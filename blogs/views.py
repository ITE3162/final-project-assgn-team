from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from blogs.models import Post

# Create your views here.

"""Here is a blog post function that takes request"""


def blog_post(request):
    results = Post.objects.all()
    return render(request, 'blog/blog_post.html', {'results': results})


def post_detail(request, slug):
    detail = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'detail': detail})


def search_post(request):
    if request.method == "POST":
        searched = request.POST.get('searched-value')
        matches = Post.objects.filter(title__contains=searched)
        return render(request, 'blog/search.html', {'values': searched, 'matches':matches})
    else:
        return render(request, 'blog/search.html')
