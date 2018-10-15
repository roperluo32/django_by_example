from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

# class PostListView(generic.ListView):
#     query_set = Post.published.all()
#     template_name = 'blog/list.html'
    

def post_list(request):
    posts = Post.published.all()

    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='post',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    return render(request, 'blog/detail.html', {'post': post})
