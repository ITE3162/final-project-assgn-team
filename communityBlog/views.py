from django.core.mail import send_mail
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


