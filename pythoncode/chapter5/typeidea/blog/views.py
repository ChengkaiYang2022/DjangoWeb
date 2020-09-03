from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from blog.models import Tag, Post, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

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
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                category = None
            else:
                p_list = p_list.filter(category_id=category_id)

    context = {
        'category': category,
        'tag': tag,
        'p_list': p_list,
    }

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return render(request, 'blog/detail.html', context={'post': post})

