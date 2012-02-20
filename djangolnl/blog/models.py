import datetime
from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)

admin.site.register(BlogPost)
