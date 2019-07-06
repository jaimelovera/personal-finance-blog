from django.conf import settings
from django.db import models
from django.utils import timezone
import os


class Post(models.Model):
    categories = (
        ('FRUGALITY', 'FRUGALITY'),
        ('INVESTING', 'INVESTING'),
        ('CREDIT_CARDS', 'CREDIT CARDS'),
    )
    featured = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )

    is_featured = models.CharField(max_length=3, choices=featured, default='NO')
    category = models.CharField(max_length=20, choices=categories)
    image= models.ImageField(upload_to="blog/static/blog/img", help_text="<h3>This is required and image must be 1200 x 800</h3>")
    title = models.CharField(max_length=200)
    body_html = models.TextField(verbose_name="body (HTML)", help_text="Use the following html tags: p, h1, h2 (paragrah, bold text, quote)")
    published_date = models.DateTimeField(default=None,blank=True, null=True, help_text="Post will not be published until this field is set (Leave blank for draft)")

    def __str__(self):
        return self.title
