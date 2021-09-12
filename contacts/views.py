
from django.shortcuts import render
from .models import ContactInfo


# Create your views here.

def contact(request):
    if request.method == "POST":

        sender = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['body']

        contact_instance = ContactInfo(sender=sender, subject=subject, message=message)

        contact_instance.save()

        return render(request, 'contacts/success-contact.html', {'context': sender})
    else:
        return render(request, 'homepage.html')
