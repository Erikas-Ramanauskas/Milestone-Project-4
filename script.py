import json
import random
from products.models import Quality  # Import your Quality model from Django

# Load the existing products from the fixture file
with open('products.json', 'r') as file:
    products_data = json.load(file)

# Fetch all quality objects from the database
qualities = list(Quality.objects.all())

# Loop through each product and assign a random quality
for product in products_data:
    # Assign a random quality ID to the product
    product['fields']['quality'] = random.choice(qualities).pk

# Save the updated products data back to the JSON file
with open('Updated_products.json', 'w') as file:
    json.dump(products_data, file, indent=2)
