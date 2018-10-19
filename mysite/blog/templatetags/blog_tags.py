from django import template
from ..models import Post
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.filter(status='post').count()

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts(count=5):
    posts = Post.published.order_by('publish')[:count]
    return {'my_posts':posts}

@register.simple_tag
def get_most_commented_posts(count=5):  
    posts = Post.published.annotate(count_comment=Count('comments')).order_by('-count_comment')[:count]
    print('get most commented posts:', posts)
    return posts

@register.filter(name='markdown')
def markdown_file(text):
    return mark_safe(markdown.markdown(text))