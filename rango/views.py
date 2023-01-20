from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    about_link = "<a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there partner! \n" + about_link)

def about(request):
    home_link = "<a href='/rango/'>Index</a>"
    return HttpResponse("Rango says here is the about page." + home_link)
