from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('investing', views.investing, name='investing'),
    path('frugality', views.frugality, name='frugality'),
    path('creditcards', views.creditcards, name='creditcards'),
]