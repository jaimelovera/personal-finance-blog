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

    category = models.CharField(max_length=20, choices=categories)
    is_featured = models.CharField(max_length=3, choices=featured, default='NO')
    image= models.ImageField(upload_to="blog/static/blog/img", help_text="Image must be 1200 x 800")
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
