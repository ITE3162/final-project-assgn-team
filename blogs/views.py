from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic import ListView

from . import forms
from blogs.models import Post
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
# Create your views here.

"""Here is a blog post function that takes request"""


def blog_post(request, tag_slug=None):
    results = Post.objects.all()
    # tag_slug = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        relates = results.filter(tags__in=[tag])
        return render(request, 'blog/related.html', {'relates': relates, 'tag': tag})
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
            form.save_m2m()  # saving tag with this method found on form not on instance
            return redirect('blogs:blog_home')
    else:
        form = forms.CreatePost()
    return render(request, 'blog/post_create.html', {'myform': form})


# def detailed_view(request, slug):
#     post = get_object_or_404(Post, tags=slug)
#     return render(request, 'blog/post_detail.html', {'query':post})


# def tagged(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     query = Post.objects.filter(tags=tag)
#     return render(request, 'blogs/blog_post.html', {'query': query})

# def detail_view(request, slug):
#     post = get_object_or_404(Post, slug)
#     return render(request, 'blog/post_detail.html' ,{'post':post })