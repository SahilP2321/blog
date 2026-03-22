from django.urls import path 
from . import views
urlpatterns = [
    #category crud
    path('',views.dashboard , name="dashboard"),
    path('categories/' ,views.categories , name='categories'),
    path('categories/add/' ,views.add_category , name='add_category'),
    path('categories/edit/<int:pk>' ,views.edit_category , name='edit_category'),
    path('categories/delete/<int:pk>' ,views.delete_category , name='delete_category'),

    #blog post crud
    path('posts/',views.posts,name='posts'),
    path('posts/new_post',views.new_post,name='new_post'),
    path('posts/delete_post/<int:pk>',views.delete_post,name='delete_post'),
    path('posts/edit_post/<int:pk>',views.edit_post,name='edit_post'),
]

