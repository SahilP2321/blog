from .models import Category , Sociallinks

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def social_links(request):
    links = Sociallinks.objects.all()
    return {'social_links': links}