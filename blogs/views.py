from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog 

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status="Published", category_id=category_id).order_by('-updated_at')
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, 'post_by_category.html', context)