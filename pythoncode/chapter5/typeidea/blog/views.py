from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        p_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        p_list, category = Post.get_by_category(category_id)
    else:
        p_list = Post.latest_posts()

    context = {
        'category': category,
        'sidebars': SideBar.get_all(),
        'tag': tag,
        'p_list': p_list,
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


# def post_detail(request, post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#
#     context = {
#         'post': post,
#         'sidebars': SideBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     return render(request, 'blog/detail.html', context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
