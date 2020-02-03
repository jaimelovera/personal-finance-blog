from django.urls import path, re_path
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('all-posts', views.all_posts, name='all-posts'),

	# Category Pages
	path('earning', views.earning, name='earning'),
	path('saving', views.saving, name='saving'),
	path('investing', views.investing, name='investing'),
	path('credit-cards', views.credit_cards, name='credit-cards'),
	path('credit-score', views.credit_score, name='credit-score'),
	path('debt', views.debt, name='debt'),
	path('mentality', views.mentality, name='mentality'),
	path('interviews', views.interviews, name='interviews'),
	path('investment-loan-calculators', TemplateView.as_view(template_name='blog/investment_loan_calculators.html'), name='investment-loan-calculators'),
	path('post/<int:pk>/<slug:slug>', views.post_detail, name='post-detail'),
	path('subscribe-thank-you', views.subscribe_thank_you, name='subscribe-thank-you'),
	path('legal', views.legal, name='legal'),
	path('contact', views.contact, name='contact'),
	path('about', views.about, name='about'),
	path('search', views.search, name='search'),
]

