from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('getmoney', views.getmoney, name='getmoney'),
    path('staybummy', views.staybummy, name='staybummy'),
]