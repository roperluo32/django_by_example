from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('author', 'publish', 'status', 'created')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ('publish', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create', 'update', 'active')
    list_filter = ('create', 'update', 'active')
    search_fields = ('name', 'email', 'body')
    ordering = ('create', 'name')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
