from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Rango Says: Here is the about page. Go back to the <a href='/rango/'>Index</a>")