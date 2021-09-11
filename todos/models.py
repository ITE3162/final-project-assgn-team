from django.db import models


# Create your models here.
class Activity(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def show_short_activity_desc(self):
        return self.description[:50] + "..."

    def __str__(self):
        return self.title
