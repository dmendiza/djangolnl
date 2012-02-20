import datetime
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)
