from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator


SHOE_SEX_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)


class Category(models.Model):
    """Model definition for Category."""

    class Meta:
        verbose_name_plural = "Categories"  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """Model definition for Brands."""

    class Meta:
        verbose_name_plural = "Brands"  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    """Model definition for ShoeSize."""

    class Meta:
        verbose_name_plural = "Sizes"  # Admin panel name

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


class Quality(models.Model):

    class Meta:
        verbose_name_plural = "Quality"  # Admin panel name

    name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        "Brand", null=True, blank=True, on_delete=models.SET_NULL
    )
    size = models.ForeignKey(
        "Size", null=True, blank=True, on_delete=models.SET_NULL
    )
    quality = models.ForeignKey(  # Add Quality field
        "Quality", null=True, blank=True, on_delete=models.SET_NULL
    )

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=254, decimal_places=2)

    shoe_sex = models.CharField(
        max_length=254, choices=SHOE_SEX_CHOICES, default="Female"
    )

    banner = models.ForeignKey(
        'ProductImage', null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name='banner')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.banner and self.image.exists():
            first_image = self.image.first()
            self.banner = first_image
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"
