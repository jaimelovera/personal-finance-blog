from django.shortcuts import render
from django.utils import timezone
from .models import Post

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/homepage.html', {'posts': posts})

def getmoney(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/getmoney.html', {'posts': posts})

def staybummy(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/staybummy.html', {'posts': posts})