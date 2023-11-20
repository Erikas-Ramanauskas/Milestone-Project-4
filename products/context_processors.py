from .models import Brand, Category, Size


def all_categories(request):

    brands = Brand.objects.all()
    categories = Category.objects.all()
    sizes = Size.objects.all()
    
    return {'brands': brands, 'categories': categories, 'sizes': sizes}