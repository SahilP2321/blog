from django.shortcuts import render ,redirect
from blogs.models import Category , Blog
from django.contrib.auth.decorators import login_required
from .forms import Categoryform , Postform , UserForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
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
        form = Categoryform(instance=category) 

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

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

@login_required(login_url='login')
def new_post(request):
    if request.method == 'POST':
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = Postform()
    context = {
        'form':form
    }
    return render(request,'dashboard/new_post.html',context)

@login_required(login_url='login')
def delete_post(request ,pk):
    post = get_object_or_404(Blog , pk=pk)
    post.delete()
    return redirect('posts')

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = Postform(instance=post)  

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/new_post.html', context)

@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request,'dashboard/users.html',context)

@login_required(login_url='login')
def add_users(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = UserForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_user.html',context)
    
@login_required(login_url='login')
def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST , instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = UserForm(instance=user)
    context = {
       'user' :user,
       'form' : form
    }
    return render(request,'dashboard/add_user.html',context)

@login_required(login_url='login')
def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')