from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Multimedia, Activity, Category

# Create your views here.
import random

def home(request):
    articles = Article.objects.all().order_by('-created_at')[:3]
    multimedia = Multimedia.objects.all()[:3]
    
    # Select a random multimedia video if available
    random_multimedia = random.choice(multimedia) if multimedia.exists() else None

    return render(request, 'home.html', {
        'articles': articles,
        'multimedia': multimedia,
        'random_multimedia': random_multimedia,
    })
def about(request):
    return render(request, 'about.html')


def article_list(request):
    # Get the category ID from the query parameters
    category_id = request.GET.get('category')
    
    # Filter articles based on the selected category
    if category_id:
        articles = Article.objects.filter(category_id=category_id)
    else:
        articles = Article.objects.all()
    
    # Fetch all categories for the dropdown
    categories = Category.objects.all()
    
    return render(request, 'articles/list.html', {
        'articles': articles,
        'categories': categories,
        'selected_category': category_id,  # Pass the selected category to the template
    })

def article_detail(request, slug):
    # Fetch the main article
    article = get_object_or_404(Article, slug=slug)
    
    # Fetch related articles based on the latest articles, excluding the current one
    related_articles = Article.objects.exclude(id=article.id).order_by('-created_at')[:3]
    
    return render(request, 'articles/detail.html', {
        'article': article,
        'related_articles': related_articles
    })


# Multimedia Views
def multimedia_list(request):
    multimedia = Multimedia.objects.all().order_by('-created_at')
    return render(request, 'multimedia/list.html', {'multimedia': multimedia})

def multimedia_detail(request, id):
    media = get_object_or_404(Multimedia, id=id)
    # Fetch related multimedia, excluding the current one
    related_multimedia = Multimedia.objects.exclude(id=media.id).order_by('-created_at')[:3]
    return render(request, 'multimedia/detail.html', {
        'multimedia': media,
        'related_multimedia': related_multimedia
    })

# Activity Views
def activity_list(request):
    activities = Activity.objects.all().order_by('-created_at')
    return render(request, 'activities/list.html', {'activities': activities})

def activity_detail(request, id):
    activity = get_object_or_404(Activity, id=id)
    # Fetch articles associated with this activity
    related_articles = activity.articles.all()
    return render(request, 'activities/detail.html', {
        'activity': activity,
    })

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')
