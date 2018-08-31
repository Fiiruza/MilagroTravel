from django.db import models
from django.utils import timezone


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='tour_images')

    def __str__(self):
        return self.title


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(default=None)
    published_date = models.DateTimeField(default=timezone.now)

    def as_dict(self):
        post = {
            'title': self.title,
            'content': self.content,
            'image': self.image.url
        }
        return post

    def __str__(self):
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name+" "+self.message

