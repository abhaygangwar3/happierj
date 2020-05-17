from django.shortcuts import render, get_object_or_404
from .models import BlogModel


def all_blogs(request):
    projects = BlogModel.objects.order_by('-date')
    return render(request, 'blog/blog_page.html', {'blogs': projects})


def detail_blog(request, blog_id):
    _id = get_object_or_404(BlogModel, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_id': _id})
