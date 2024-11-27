from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'articles': articles})

def about(request):
    return render(request, 'about.html')

def activities(request):
    return render(request, 'activities.html')


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/detail.html', {'article': article})



def multimedia(request):
    return render(request, 'multimedia.html')

def contact(request):
    return render(request, 'contact.html')  
