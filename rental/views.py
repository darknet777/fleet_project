from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'rental/home.html')

def pricing(request):
    return render(request, 'rental/pricing.html')

def gallery(request):
    return render(request, 'rental/gallery.html')

def about(request):
    return render(request, 'rental/about.html')

def contact(request):
    return render(request, 'rental/contact.html')
