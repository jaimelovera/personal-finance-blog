import os
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

def validate_image(image):
    file_height = image.height 
    file_width = image.width
    if file_width/file_height != 3/2:
        raise ValidationError("Image aspect ratio must be exactly 3:2 </br> i.e. 1200 x 800")

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
    main_image = models.ImageField(upload_to="blog/static/blog/img", validators=[validate_image], help_text="Aspect ratio must be exactly 3:2 </br> i.e. 1200 x 800")
    inline_image_1 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_2 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_3 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_4 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_5 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_6 = models.ImageField(upload_to="blog/static/blog/img", null=True, blank=True, default=None, help_text="Optional")
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, editable=False)
    body_html = models.TextField(verbose_name="body (HTML)", help_text="<p> Use the following tags:</br> <xmp><h1>Bold Header</h1></xmp> <xmp><p>Paragraph</p></xmp> <xmp><h2>Quote</h2></xmp> <xmp><a href='url' target='_blank'>Link</a></xmp> <xmp><img1> - <img6></xmp> </p>")
    published_date = models.DateTimeField(default=None,blank=True, null=True, help_text="Post will not be published until this field is set </br> *Leave blank for draft")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
