from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog 

def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status="Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")
    context = {
        "featured_post": featured_post,
        "posts": posts,
    }
    return render(request, 'home.html', context)

