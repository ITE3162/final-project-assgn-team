from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from . import forms
from blogs.models import Post
from django.core.mail import send_mail

# Create your views here.

"""Here is a blog post function that takes request"""


def blog_post(request):
    results = Post.objects.all()
    if len(results) == 0:
        empty_msg = "No post to show"
        return render(request, 'blog/blog_post.html', {'empty': empty_msg})
    else:
        return render(request, 'blog/blog_post.html', {'results': results})


def post_detail(request, slug):
    detail = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'detail': detail})


def search_post(request):
    if request.method == "POST":
        searched = request.POST.get('searched-value')
        matches = Post.objects.filter(title__contains=searched)
        return render(request, 'blog/search.html', {'values': searched, 'matches': matches})
    else:
        return render(request, 'blog/search.html')


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  # Pre-saving
            instance.author = request.user  # adding user as Author to the instance of post
            instance.save()  # saving post with author
            return redirect('blogs:blog_home')
    else:
        form = forms.CreatePost()
    return render(request, 'blog/post_create.html', {'myform': form})
