from django.db import models


# Create your models here.
class AboutUs(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(default='logo-about.png')
