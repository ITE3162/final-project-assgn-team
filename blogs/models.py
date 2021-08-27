from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def short_body(self):
        return self.body[:50] + "..."


