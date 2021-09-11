from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='profile-default.jpg', blank=True, verbose_name='Profile-Pic')
