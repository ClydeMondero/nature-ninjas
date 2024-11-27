from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def activities(request):
    return render(request, 'activities.html')

def articles(request):
    return render(request, 'articles.html')

def multimedia(request):
    return render(request, 'multimedia.html')

def contact(request):
    return render(request, 'contact.html')  
