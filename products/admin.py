from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'description',
        'image',
        'image_alt',
        'shoe_size',
        'shoe_sex',
        'shoe_type',
        'shoe_brand',
    )
    
    list_filter = (
        'price',
        'shoe_size',
        'shoe_sex',
        'shoe_type',
        'shoe_brand',
    )