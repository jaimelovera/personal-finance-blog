from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'published_date')
    list_filter = ('category', 'is_featured', 'published_date')

admin.site.register(Post, PostAdmin)