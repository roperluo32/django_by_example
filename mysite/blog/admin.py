from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('author', 'publish', 'status', 'created')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ('publish', 'author')

admin.site.register(Post, PostAdmin)
