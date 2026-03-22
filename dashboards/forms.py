from django import forms
from blogs.models import Category ,Blog

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class Postform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')

        labels = {
            'title': 'Post Title',
            'category': 'Choose Category',
            'featured_image': 'Upload Featured Image',
            'short_description': 'Short Description',
            'blog_body': 'Blog Content',
            'status': 'Publish Status',
            'is_featured': 'Mark as Featured',
        }

    