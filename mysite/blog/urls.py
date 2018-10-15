from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
