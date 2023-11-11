from django.contrib import admin
from .models import Product, Category, Brand, Size


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
