from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('product_detail/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)