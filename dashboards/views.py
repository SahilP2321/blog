from django.shortcuts import render ,redirect
from blogs.models import Category , Blog
from django.contrib.auth.decorators import login_required
from .forms import Categoryform
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_counts':category_counts,
        'blogs_count':blogs_count,
    }
    
    return render(request,'dashboard/dashboard.html',context)


def categories(request):
    category =Category.objects.all()
    context = {
        'category':category
    }
    return render(request,'dashboard/categories.html',context)

@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = Categoryform()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)


@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = Categoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = Categoryform(instance=category)  # ✅ for GET

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login')
def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')