from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from blog.models import Tag, Post


def post_list(request, category_id=None, tag_id=None):
    content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(
        category_id=category_id,
        tag_id=tag_id,
    )
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            p_list = []
        else:
            p_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        p_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            p_list = p_list.filter(category_id=category_id)

    return render(request, 'blog/list.html', context={'post': p_list})


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return render(request, 'blog/detail.html', context={'post': post})

