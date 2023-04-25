from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    context = locals()
    template = 'home.html',
    return render(request, template, context) #string of HTML code

def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact Page<h1>') #string of HTML code

