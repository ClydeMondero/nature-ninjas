from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('activities/', views.activities, name='activities'),  # Activities page
    path('articles/', views.articles, name='articles'),  # Articles page
    path('multimedia/', views.multimedia, name='multimedia'),  # Multimedia page
]
