from django.urls import path, re_path
from . import views
from blog.feeds import LatestPostFeeds

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
    path('feed/', LatestPostFeeds(), name='post_feed'),
]
