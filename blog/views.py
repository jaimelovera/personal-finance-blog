from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from functools import reduce
from django.conf import settings
from django.db.models import Q, Value, IntegerField
from django.core.paginator import Paginator
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

        objects = posts_title_and.union(posts_body_and, posts_title_or, posts_body_or).order_by("order")
        count = objects.count()
        paginator = Paginator(objects, 30)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        return render(request, 'blog/search.html', {'query': query, 'count': count, 'posts': posts})
    else:
        objects = Post.objects.none()
        query = ''
        count = 0
        paginator = Paginator(objects, 30, allow_empty_first_page=True)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        return render(request, 'blog/search.html', {'query': query, 'count': count, 'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def subscribe_thank_you(request):
    return render(request, 'blog/subscribe_thank_you.html')

def legal(request):
    return render(request, 'blog/legal.html')

def homepage(request):
    posts = Post.objects.filter(is_featured='yes').exclude(published_date=None).order_by('-published_date')
    posts2 = Post.objects.filter(is_featured='no').exclude(published_date=None).order_by('-published_date')[:30]
    return render(request, 'blog/homepage.html', {'posts': posts, 'posts2': posts2})

def all_posts(request):
    objects = Post.objects.exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/all_posts.html', {'posts': posts})

def post_detail(request, pk, slug):
    #Checks for superuser authentication first. To preview unpublished posts using 'View on site' admin model link.
    if request.user.is_superuser:
        posts = Post.objects
    else:
        posts = Post.objects.exclude(published_date=None)
    post = get_object_or_404(posts, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


# Category Pages
def earning(request):
    objects = Post.objects.filter(category='earning').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/earning.html', {'posts': posts})

def saving(request):
    objects = Post.objects.filter(category='saving').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/saving.html', {'posts': posts})

def investing(request):
    objects = Post.objects.filter(category='investing').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/investing.html', {'posts': posts})

def personal_finance(request):
    objects = Post.objects.filter(Q(category='debt') | Q(category='credit-score') | Q(category='credit-cards') | Q(category='mentality')).exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/personal_finance.html', {'posts': posts})

def credit_cards(request):
    objects = Post.objects.filter(category='credit-cards').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/credit_cards.html', {'posts': posts})

def credit_score(request):
    objects = Post.objects.filter(category='credit-score').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/credit_score.html', {'posts': posts})

def debt(request):
    objects = Post.objects.filter(category='debt').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/debt.html', {'posts': posts})

def mentality(request):
    objects = Post.objects.filter(category='mentality').exclude(published_date=None).order_by('-published_date')
    paginator = Paginator(objects, 30)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/mentality.html', {'posts': posts})
