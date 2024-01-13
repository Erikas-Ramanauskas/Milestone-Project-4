from django.contrib import admin
from .models import Product, Category, Brand, Size, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "price",
        "size",
        "shoe_sex",
        "sold",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        "uk_name",
        "eu_name",
        "us_m_name",
        "us_w_name",
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    list_filter = ('product',)
    search_fields = ('product__name', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
