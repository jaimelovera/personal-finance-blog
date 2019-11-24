from django.urls import path, re_path
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('all-posts', views.all_posts, name='all-posts'),
	path('investing', views.investing, name='investing'),
	path('saving', views.saving, name='saving'),
	path('creditcards', views.creditcards, name='creditcards'),
	path('money-visualizer', TemplateView.as_view(template_name='blog/money_visualizer.html'), name='money-visualizer'),
	path('post/<int:pk>/<slug:slug>', views.post_detail, name='post-detail'),
	path('subscribe-thank-you', views.subscribe_thank_you, name='subscribe-thank-you'),
	path('legal', views.legal, name='legal'),
	path('contact', views.contact, name='contact'),
	path('about', views.about, name='about'),
	path('search', views.search, name='search'),

]

