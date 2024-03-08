from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse("<html><body><h1>Home</h1><a href='/about/'> About Page</a></body></html>")

def about(request):
    return HttpResponse("<html><body><h1>About</h1><a href='/ /'>Home view</a> | <a href='/contact/'>Contact View</a></body></html>")

def contact(request):
    return HttpResponse("<html><body><h1>Contact view</h1><a href='/about/'>About </a> | <a href='/category/'> To categories</a></body></html>")

def category(request):
    return HttpResponse("<html><body><h1>Category page</h1><a href='/contact/'>Contact</a> | <a href='/about/'>Move to about</a></body></html>")