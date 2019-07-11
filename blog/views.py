from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404

def not_found_404(request, exception):
    return render(request, 'blog/404.html', status=404)

def subscribe(request):
    return render(request, 'blog/subscribe.html')

def subscribe_thank_you(request):
    return render(request, 'blog/subscribe-thank-you.html')

def homepage(request):
    posts = Post.objects.filter(is_featured='YES').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/homepage.html', {'posts': posts})

def frugality(request):
    posts = Post.objects.filter(category='FRUGALITY').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/frugality.html', {'posts': posts})

def investing(request):
    posts = Post.objects.filter(category='INVESTING').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/investing.html', {'posts': posts})

def creditcards(request):
    posts = Post.objects.filter(category='CREDIT_CARDS').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/creditcards.html', {'posts': posts})

def post_detail(request, pk):
    posts = Post.objects.exclude(published_date=None)
    post = get_object_or_404(posts, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

