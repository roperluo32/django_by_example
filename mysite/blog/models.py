from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='post')

class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('post', 'Post'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(choices=STATUS_CHOICE, default='draft', max_length=10)

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse('blog:post_detail', args=(self.publish.year,
                                            self.publish.strftime("%m"),
                                            self.publish.strftime("%d"),
                                            self.slug)) 

    objects = models.Manager()
    published = PublishedManager()


class Comment(models.Model):
    post = models.ForeignKey("Post", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)