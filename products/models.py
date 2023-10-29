from django.db import models
from django_resized import ResizedImageField


class Category(models.Model):
    """ Model definition for Category. """
    class Meta:
        verbose_name_plural = 'Categories'  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model definition for Product.
    """
    
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75 , upload_to='products/', force_format='WEBP', null=True, blank=True)
    image_alt = models.CharField(max_length=255,null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shoe_size = models.CharField(max_length=10)
    shoe_sex = models.CharField(max_length=10)
    shoe_type = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    shoe_brand = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    
    
    


