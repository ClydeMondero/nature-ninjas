from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('activities/', views.activities, name='activities'),  # Activities page
    path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('multimedia/', views.multimedia, name='multimedia'),  # Multimedia page
    path('contact/', views.contact, name='contact'),  # Contact Us Page
]
