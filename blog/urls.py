from django.urls import path
from . import views 

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('investing', views.investing, name='investing'),
	path('frugality', views.frugality, name='frugality'),
	path('creditcards', views.creditcards, name='creditcards'),
	path('post/<int:pk>/<slug:slug>', views.post_detail, name='post_detail'),
	path('subscribe-thank-you', views.subscribe_thank_you, name='subscribe_thank_you'),
	path('legal', views.legal, name='legal'),
	path('contact', views.contact, name='contact'),
	path('about', views.about, name='about'),
	path('search', views.search, name='search'),
]

