from .models import Brand, Category


def all_categories(request):
    # Get distinct brands, categories acording to sex
    male_brands = Brand.objects.filter(
        product__isnull=False, product__shoe_sex="male").distinct()
    male_categories = Category.objects.filter(
        product__isnull=False, product__shoe_sex="male").distinct()

    female_brands = Brand.objects.filter(
        product__isnull=False, product__shoe_sex="female").distinct()
    female_categories = Category.objects.filter(
        product__isnull=False, product__shoe_sex="female").distinct()

    return {'male_brands': male_brands, 'male_categories': male_categories, 'female_brands': female_brands, 'female_categories': female_categories}
