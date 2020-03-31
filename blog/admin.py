from django.contrib import admin
from .models import Post, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'category', 'is_featured', 'published_date')
    list_filter = ('category', 'is_featured', 'published_date')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)