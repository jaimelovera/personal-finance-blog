from django.conf import settings
from django.db import models
from django.utils import timezone
import os
from django.core.exceptions import ValidationError

def validate_image(image):
    file_height = image.height 
    file_width = image.width
    if (file_width != 1200) or (file_height != 800):
        raise ValidationError("Image must be 1200 x 800")

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
    image= models.ImageField(upload_to="blog/static/blog/img", validators=[validate_image], help_text="Image must be 1200 x 800")
    title = models.CharField(max_length=200)
    body_html = models.TextField(verbose_name="body (HTML)", help_text="Use the following html tags:</br>h1:bold header</br>p:paragrah</br>h2:quote")
    published_date = models.DateTimeField(default=None,blank=True, null=True, help_text="Post will not be published until this field is set (Leave blank for draft)")

    def __str__(self):
        return self.title
