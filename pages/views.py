from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return HttpResponse ("<h1>Hello world</h1>")   #string of html code

def contact_view(request, *args, **kwargs):
    return HttpResponse ("<h1>Contact Page</h1>")

def about_view(request,*args, **kwargs):
    return HttpResponse ("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
    return HttpResponse ("<h1>Social Page</h1>")