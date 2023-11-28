from .models import Brand, Category, Size, Product

def all_categories(request):
    # Get distinct brands, categories, and sizes that belong to at least one product
    brands = Brand.objects.filter(product__isnull=False).distinct()
    categories = Category.objects.filter(product__isnull=False).distinct()
    sizes = Size.objects.filter(product__isnull=False).distinct()
    
    return {'brands': brands, 'categories': categories, 'sizes': sizes}
