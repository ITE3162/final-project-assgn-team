from django.core.mail import send_mail
from django.shortcuts import render
from blogs.models import Post
from about.models import AboutUs
from teams.models import Team
from todos.models import Activity


def homepage(request):
    blogs = Post.objects.all().order_by("title")
    about = AboutUs.objects.all()
    todos = Activity.objects.all().order_by("title")
    mates = Team.objects.all()
    return render(request, 'homepage.html', {'blogs': blogs, 'aboutus':about, 'todos':todos, 'teams':mates})

