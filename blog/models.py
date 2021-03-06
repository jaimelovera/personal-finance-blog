from django.template.defaultfilters import slugify
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

def validate_image(image):
    file_height = image.height
    file_width = image.width
    if file_width/file_height != 3/2:
        raise ValidationError("Image aspect ratio must be exactly 3:2 </br> i.e. 1200 x 800")


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    categories = (
        ('earning', 'Earning'),
        ('saving', 'Saving'),
        ('investing', 'Investing'),
        ('credit-cards', 'Credit Cards'),
        ('credit-score', 'Credit Score'),
        ('debt', 'Debt'),
        ('mentality', 'Mentality'),
        ('interviews', 'Interviews'),
    )
    featured = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    is_featured = models.CharField(max_length=3, choices=featured, default='no')
    category = models.CharField(max_length=20, choices=categories)
    main_image = models.ImageField(upload_to="img", validators=[validate_image], help_text="<h3>Aspect ratio must be exactly 3:2 </br> i.e. 1200 x 800</h3>")
    inline_image_1 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_2 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_3 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_4 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_5 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    inline_image_6 = models.ImageField(upload_to="img", null=True, blank=True, default=None, help_text="Optional")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True, editable=False)
    body_html = models.TextField(verbose_name="body (HTML)", help_text="<h3> Use the following tags:</br> <xmp><p>Paragraph</p></xmp> <xmp><h1>Bold Header</h1></xmp> <xmp><h2>Quote</h2></xmp> <xmp><ul><li>Bullet Points</li></ul></xmp> <xmp><a href='https'>Link</a></xmp> <xmp><button><a href='https'>Button</a></button></xmp> <xmp><img1> - <img6></xmp> </h3>")
    published_date = models.DateTimeField(default=None,blank=True, null=True, help_text="<h3>Post will not be published until this field is set </br> *Leave blank for draft</h3>")

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk, 'slug':self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
