from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
import operator
from functools import reduce

def not_found_404(request, exception):
    return render(request, 'blog/404.html', status=404)

def contact(request):
    return render(request, 'blog/contact.html')

def search(request):
    query = request.GET.get('query')
    if query:
        query_list = query.split()
        posts=Post.objects.exclude(published_date=None).filter(reduce(operator.or_,(Q(title__icontains=q) for q in query_list)) | reduce(operator.or_,(Q(body_html__icontains=q) for q in query_list)))
        return render(request, 'blog/search.html', {'query': query, 'posts': posts})
    else:
        posts=None
        query=''
        return render(request, 'blog/search.html', {'query': query, 'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def subscribe_thank_you(request):
    return render(request, 'blog/subscribe_thank_you.html')

def legal(request):
    return render(request, 'blog/legal.html')

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

def post_detail(request, pk, slug):
    posts = Post.objects.exclude(published_date=None)
    post = get_object_or_404(posts, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

