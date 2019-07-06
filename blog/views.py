from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def homepage(request):
    posts = Post.objects.filter(is_featured='YES').order_by('-published_date')
    return render(request, 'blog/homepage.html', {'posts': posts})

def frugality(request):
    posts = Post.objects.filter(category='FRUGALITY').order_by('-published_date')
    return render(request, 'blog/frugality.html', {'posts': posts})

def investing(request):
    posts = Post.objects.filter(category='INVESTING').order_by('-published_date')
    return render(request, 'blog/investing.html', {'posts': posts})

def creditcards(request):
    posts = Post.objects.filter(category='CREDIT_CARDS').order_by('-published_date')
    return render(request, 'blog/creditcards.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

