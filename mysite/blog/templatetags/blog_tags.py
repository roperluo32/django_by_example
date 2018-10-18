from django import template
from ..models import Post
register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.filter(status='post').count()

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts(count=5):
    print('count:', count)
    posts = Post.objects.all().order_by('publish')[:count]
    print(posts)
    return {'my_posts':posts}