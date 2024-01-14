from .models import Brand, Category, Size


def all_categories(request):
    # Get distinct brands, categories acording to sex and if products are sold
    male_brands = Brand.objects.filter(
        product__isnull=False, product__shoe_sex="male", product__sold=False).distinct()
    male_categories = Category.objects.filter(
        product__isnull=False, product__shoe_sex="male", product__sold=False).distinct()
    male_sizes = Size.objects.filter(
        product__isnull=False, product__shoe_sex="male", product__sold=False).distinct().order_by('eu_name')
    male_sizes = sorted(male_sizes, key=lambda x: int(
        x.get_eu_name()) if x.get_eu_name().isdigit() else float('inf'), reverse=True)

    female_brands = Brand.objects.filter(
        product__isnull=False, product__shoe_sex="female", product__sold=False).distinct()
    female_categories = Category.objects.filter(
        product__isnull=False, product__shoe_sex="female", product__sold=False).distinct()
    female_sizes = Size.objects.filter(
        product__isnull=False, product__shoe_sex="female", product__sold=False).distinct().order_by('eu_name')
    female_sizes = sorted(female_sizes, key=lambda x: int(
        x.get_eu_name()) if x.get_eu_name().isdigit() else float('inf'), reverse=True)

    return {'male_brands': male_brands, 'male_categories': male_categories, 'male_sizes': male_sizes,
            'female_brands': female_brands, 'female_categories': female_categories, 'female_sizes': female_sizes}
