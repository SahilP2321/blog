from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog ,About , Sociallinks

def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status="Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        "featured_post": featured_post,
        "posts": posts,
        "about":about,
    }
    return render(request, 'home.html', context)

