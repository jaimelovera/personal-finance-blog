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
    query_list = list(set(query_list)) #remove duplicate words
    stop_words = []
    #opens file with stop words.
    with open(os.path.join(settings.BASE_DIR, 'blog', 'stop_words.txt')) as f:
        stop_words = f.read().splitlines()
    #removes stop words.
    for word in stop_words:
        while word in query_list: query_list.remove(word)
    if query_list:
        #A simple search query. Temporary while I use SQLite.
        posts = Post.objects.exclude(published_date=None)

        #AND title/body
        posts_title_and = posts.filter(
            reduce(operator.and_,(Q(title__icontains=word) for word in query_list))).annotate(order=Value(1, IntegerField()))
        posts_body_and =  posts.exclude(pk__in=posts_title_and).filter(
            reduce(operator.and_,(Q(body_html__icontains=word) for word in query_list))).annotate(order=Value(3, IntegerField()))

        #OR title/body
        posts_title_or = posts.exclude(pk__in=(posts_title_and|posts_body_and)).filter(
            reduce(operator.or_,(Q(title__icontains=word) for word in query_list))).annotate(order=Value(2, IntegerField()))
        posts_body_or =  posts.exclude(pk__in=(posts_title_and|posts_body_and|posts_title_or)).filter(
            reduce(operator.or_,(Q(body_html__icontains=word) for word in query_list))).annotate(order=Value(4, IntegerField()))

        posts = posts_title_and.union(posts_body_and, posts_title_or, posts_body_or).order_by("order")[:21]
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

def tools(request):
    return render(request, 'blog/tools.html')

def post_detail(request, pk, slug):
    #Checks for superuser authentication first. To preview unpublished posts using 'View on site' admin model link.
    if request.user.is_superuser:
        posts = Post.objects
    else:
        posts = Post.objects.exclude(published_date=None)
    post = get_object_or_404(posts, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
