from django.conf import settings
from django.db import models
from django.utils import timezone
import os


class Post(models.Model):
    categories = (
        ('FRUGALITY', 'Frugality'),
        ('INVESTING', 'Investing'),
        ('CREDIT_CARDS', 'Credit Cards'),
    )
    featured = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )

    is_featured = models.CharField(max_length=3, choices=featured, default='NO')
    category = models.CharField(max_length=20, choices=categories)
    image= models.ImageField(upload_to="blog/static/blog/img", help_text="This is required and image must be 1200 x 800")
    title = models.CharField(max_length=200)
    body_html = models.TextField(verbose_name="body (HTML)")
    published_date = models.DateTimeField(default=None,blank=True, null=True)

    def __str__(self):
        return self.title
