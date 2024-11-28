from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
     path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('multimedia/', views.multimedia_list, name='multimedia'),
    path('multimedia/<int:id>/', views.multimedia_detail, name='multimedia_detail'),
    path('activities/', views.activity_list, name='activities'),
    path('activities/<int:id>/', views.activity_detail, name='activity_detail'),
    path('contact/', views.contact, name='contact'),  # Contact Us Page
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
