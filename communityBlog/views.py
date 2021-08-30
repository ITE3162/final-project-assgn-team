from django.core.mail import send_mail
from django.shortcuts import render
from blogs.models import Post


def homepage(request):
    blogs = Post.objects.all().order_by("title")
    return render(request, 'homepage.html', {'blogs': blogs})

