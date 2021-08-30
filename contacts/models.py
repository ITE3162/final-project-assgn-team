from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    contacted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
