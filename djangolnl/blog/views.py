from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<html><body><h1>Hello, World!</h1></body</html>')
