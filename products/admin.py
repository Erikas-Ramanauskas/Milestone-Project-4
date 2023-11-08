from django.contrib import admin
from .models import Product, Category, Size, Brand


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Brand)
