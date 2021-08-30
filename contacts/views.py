from django.http import HttpResponse
from django.shortcuts import render
from .models import ContactInfo
from blogs.models import Post


# Create your views here.
def contact(request):
    blogs = Post.objects.all().order_by("title")
    if request.method == "POST":

        sender = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['body']

        contact_instance = ContactInfo(sender=sender, subject=subject, message=message)

        contact_instance.save()
        return render(request, 'homepage.html', {'context': sender, 'blogs': blogs})
    else:
        return render(request, 'homepage.html', {'blogs': blogs})
    # if request.method == "POST":
    #     msg_email = request.POST['email']
    #     msg_subject = request.POST['subject']
    #     msg_body = request.POST['text']
    #
    #     # send_mail(
    #     #     msg_subject,
    #     #     msg_body,
    #     #     msg_email,
    #     #     ['nyakamweaimable@gmail.com']
    #     # )
    #     return render(request, 'homepage.html', {'message_name': msg_email})
    # else:
    #     return render(request, 'homepage.html')
