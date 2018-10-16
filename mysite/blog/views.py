from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .forms import EmailPostForm
# Create your views here.

# class PostListView(generic.ListView):
#     query_set = Post.published.all()
#     template_name = 'blog/list.html'

def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id)    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #发送邮件

            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/share.html', {'post': post, 'form': form, 'sent': sent})

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
