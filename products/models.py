from django.db import models
from django_resized import ResizedImageField


SHOE_TYPE_CHOICES = (
    ("sneakers", "Sneakers"),
    ("sandals", "Sandals"),
    ("boots", "Boots"),
    ("flats", "Flats"),
    ("high_heels", "High Heels"),
    ("loafers", "Loafers"),
    ("running_shoes", "Running Shoes"),
    ("basketball_shoes", "Basketball Shoes"),
    ("tennis_shoes", "Tennis Shoes"),
    ("hiking_boots", "Hiking Boots"),
    ("rain_boots", "Rain Boots"),
    ("ankle_boots", "Ankle Boots"),
    ("platform_shoes", "Platform Shoes"),
    ("mules", "Mules"),
    ("chukka_boots", "Chukka Boots"),
    ("cowboy_boots", "Cowboy Boots")
)

#  ("UK", "EU", "US Men's", "US Women's"),
SHOE_SIZE_CHOICES = (
    (2, "2"),
    (2.5, "2.5"),
    (3, "3"),
    (3.5, "3.5"),
    (4, "4"),
    (4.5, "4.5"),
    (5, "5"),
    (5.5, "5.5"),
    (6, "6"),
    (6.5, "6.5"),
    (7, "7"),
    (7.5, "7.5"),
    (8, "8"),
    (8.5, "8.5"),
    (9, "9"),
    (9.5, "9.5"),
    (10, "10"),
    (10.5, "10.5"),
    (11, "11"),
    (11.5, "11.5"),
    (12, "12"),
    (12.5, "12.5"),
    (13, "13"),
    (13.5, "13.5"),
    (14, "14"),
    (14.5, "14.5")
)

SHOE_BRAND_CHOICES = (
    ("nike", "Nike"),
    ("adidas", "Adidas"),
    ("puma", "Puma"),
    ("reebok", "Reebok"),
    ("converse", "Converse"),
    ("new_balance", "New Balance"),
    ("vans", "Vans"),
    ("under_armour", "Under Armour"),
    ("skechers", "Skechers"),
    ("asics", "ASICS"),
    ("brooks", "Brooks"),
    ("clarks", "Clarks"),
    ("timberland", "Timberland"),
    ("dr_martens", "Dr. Martens"),
    ("fila", "FILA"),
    ("merrell", "Merrell"),
    ("salomon", "Salomon"),
    ("ecco", "Ecco"),
    ("lacoste", "Lacoste"),
    ("saucony", "Saucony"),
    ("vionic", "Vionic"),
    ("mizuno", "Mizuno"),
    ("hoka_one_one", "Hoka One One"),
    ("under_armour", "Under Armour"),
    ("skechers", "Skechers"),
    ("birkenstock", "Birkenstock"),
    ("ugg", "UGG"),
    ("cole_haan", "Cole Haan"),
    ("steve_madden", "Steve Madden"),
    ("aldo", "Aldo"),
    ("fendi", "Fendi"),
    ("gucci", "Gucci"),
    ("prada", "Prada"),
    ("versace", "Versace"),
    ("balenciaga", "Balenciaga"),
    ("louis_vuitton", "Louis Vuitton"),
    ("jimmy_choo", "Jimmy Choo"),
    ("christian_louboutin", "Christian Louboutin"),
    ("valentino", "Valentino"),
    ("dior", "Dior")
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
    
    
class Size(models.Model):
    """ Model definition for Size. """
    class Meta:
        verbose_name_plural = 'Sizes'  # Admin panel name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name    
    
    
class Brand(models.Model):
    """ Model definition for Brand. """
    class Meta:
        verbose_name_plural = 'Brands'  # Admin panel name

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75 , upload_to='products/', force_format='WEBP', null=True, blank=True)
    

    size = models.CharField(max_length=200, choices=SHOE_SIZE_CHOICES, default="8")
    shoe_sex = models.CharField(max_length=10)
    category = models.CharField(max_length=50, choices=SHOE_TYPE_CHOICES, default='Sneakers')
    brand = models.CharField(max_length=50, choices=SHOE_BRAND_CHOICES, default='Nike')

    def __str__(self):
        return self.name
    

    
    
    


