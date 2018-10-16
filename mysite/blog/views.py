from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from taggit.models import Tag
# Create your views here.

# class PostListView(generic.ListView):
#     query_set = Post.published.all()
#     template_name = 'blog/list.html'

def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id)    
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #发送邮件

            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/share.html', {'post': post, 'form': form, 'sent': sent})

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request, 'blog/list.html', {'posts': posts,
                                                'page': page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='post',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post,
                                                 'comments': comments,
                                                 'new_comment': new_comment,
                                                 'comment_form': comment_form,
                                                 })
