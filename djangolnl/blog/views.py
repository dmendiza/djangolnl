from django.shortcuts import render_to_response
from blog.models import BlogPost

# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render_to_response('home.html', {'posts': posts})
