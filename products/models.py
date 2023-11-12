from django.db import models

SHOE_SEX_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)

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
    
    
class Brand(models.Model):
    """ Model definition for Brands. """
    class Meta:
        verbose_name_plural = 'Brands'  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name    
    
    
class Size(models.Model):
    """ Model definition for ShoeSize. """
    class Meta:
        verbose_name_plural = 'Sizes'  # Admin panel name

    eu_name = models.CharField(max_length=254)
    uk_name = models.CharField(max_length=254)
    us_m_name = models.CharField(max_length=254)
    us_w_name = models.CharField(max_length=254)

    def __str__(self):
        return self.uk_name

    def get_uk_name(self):
        return self.uk_name
    
    def get_us_m_name(self):
        return self.us_m_name
    
    def get_us_w_name(self):
        return self.us_w_name
    
    def get_eu_name(self):
        return self.eu_name



class Product(models.Model):
    """
    Model definition for Product.
    """
    category = models.ForeignKey('Category', max_length=254, null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', max_length=254, null=True, blank=True, on_delete=models.SET_NULL)
    size = models.ForeignKey('Size', max_length=254, null=True, blank=True, on_delete=models.SET_NULL)
    
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=254, decimal_places=2)
    
    shoe_sex = models.CharField(max_length=254, choices=SHOE_SEX_CHOICES, default='Female')
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    """define image model"""
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)    
    file_name = models.ImageField(null=True, blank=True)
    file_url = models.URLField(max_length=1024, null=True, blank=True)