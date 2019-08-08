from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from functools import reduce
from django.conf import settings
from django.db.models import Q, Value, IntegerField
import operator
import os

def not_found_404(request, exception):
    return render(request, 'blog/404.html', status=404)

def contact(request):
    return render(request, 'blog/contact.html')

def search(request):
    query = request.GET.get('query')
    query_list = query.lower().split()
    stop_words = []

    with open(os.path.join(settings.BASE_DIR, 'blog', 'stop_words.txt')) as f:
        stop_words = f.read().splitlines()

    for word in stop_words:
        while word in query_list: query_list.remove(word) 

    if query_list:
        #A simple search query that excludes stop words and places results in order of relevance. Depending if
        #search words exist in the title+body, or just title, or just body.
        posts = Post.objects.exclude(published_date=None)
        posts_title = posts.filter(reduce(operator.or_,(Q(title__icontains=q) for q in query_list)))
        posts_body = posts.filter(reduce(operator.or_,(Q(body_html__icontains=q) for q in query_list)))
        
        posts_both = (posts_title&posts_body).annotate(order=Value(1, IntegerField()))
        posts_title = posts_title.exclude(pk__in=posts_both).annotate(order=Value(2, IntegerField()))
        posts_body = posts_body.exclude(pk__in=posts_both).annotate(order=Value(3, IntegerField()))

        posts = posts_both.union(posts_title, posts_body).order_by("order")
        count = posts.count()
        return render(request, 'blog/search.html', {'query': query, 'count': count, 'posts': posts})
    else:
        posts = None
        query = ''
        count = 0
        return render(request, 'blog/search.html', {'query': query, 'count': count, 'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def subscribe_thank_you(request):
    return render(request, 'blog/subscribe_thank_you.html')

def legal(request):
    return render(request, 'blog/legal.html')

def homepage(request):
    posts = Post.objects.filter(is_featured='YES').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/homepage.html', {'posts': posts})

def all_posts(request):
    posts = Post.objects.exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/all_posts.html', {'posts': posts})

def saving(request):
    posts = Post.objects.filter(category='SAVING').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/saving.html', {'posts': posts})

def investing(request):
    posts = Post.objects.filter(category='INVESTING').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/investing.html', {'posts': posts})

def creditcards(request):
    posts = Post.objects.filter(category='CREDIT_CARDS').exclude(published_date=None).order_by('-published_date')
    return render(request, 'blog/creditcards.html', {'posts': posts})

def post_detail(request, pk, slug):
    #Checks for superuser authentication first. To preview unpublished posts using 'View on site' admin model link.
    if request.user.is_superuser:
        posts = Post.objects
    else:
        posts = Post.objects.exclude(published_date=None)
    post = get_object_or_404(posts, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})