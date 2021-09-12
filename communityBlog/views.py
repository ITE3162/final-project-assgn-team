from django.core.mail import send_mail
from django.shortcuts import render
from blogs.models import Post
from about.models import AboutUs
from teams.models import Team
from todos.models import Activity
from contacts.models import ContactInfo


def homepage(request):
    blogs = Post.objects.all().order_by("title")
    about = AboutUs.objects.all()
    todos = Activity.objects.all().order_by("title")
    mates = Team.objects.all()

    # if request.method == "POST":
    #     sender = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['body']
    #     contact_instance = ContactInfo(sender=sender, subject=subject, message=message)
    #     contact_instance.save()
    #
    #     return render(request, 'homepage.html', {'context': sender})
    #
    # else:

    return render(request, 'homepage.html', {'blogs': blogs, 'aboutus': about, 'todos': todos, 'teams': mates})

