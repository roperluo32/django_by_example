from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostFeeds(Feed):
    title = 'My Blog'
    link = '/blog/'
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return truncatewords(obj.body, 30)

    def item_link(self, obj):
        return obj.absolute_url()