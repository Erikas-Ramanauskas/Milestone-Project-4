from .models import Category
from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Product, Category, Brand, Quality, Image, Size
from .forms import ProductForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from os.path import join


class ModelTests(TestCase):

    def setUp(self):
        # Create sample data for testing
        self.category = Category.objects.create(
            name="Test Category", friendly_name="Test Friendly Category")
        self.brand = Brand.objects.create(
            name="Test Brand", friendly_name="Test Friendly Brand")
        self.size = Size.objects.create(
            eu_name="EU42", uk_name="UK8", us_m_name="US9", us_w_name="US10")
        self.quality = Quality.objects.create(
            name="High Quality", description="Test description", rating=4)
        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            size=self.size,
            quality=self.quality,
            sku="TEST123",
            name="Test Product",
            description="Test Description",
            price=99.99,
            shoe_sex="male",
            sold=False
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_brand_str(self):
        self.assertEqual(str(self.brand), "Test Brand")

    def test_size_str(self):
        self.assertEqual(str(self.size), "UK8")

    def test_quality_str(self):
        self.assertEqual(str(self.quality), "High Quality")

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")

    # test image in a future commit


class ViewsTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        self.superuser = get_user_model().objects.create_superuser(
            username='testadmin',
            email='admin@example.com',
            password='testsuperpassword'
        )

        # Create sample data for testing
        self.category = Category.objects.create(
            name="Test Category", friendly_name="Test Friendly Category")
        self.brand = Brand.objects.create(
            name="Test Brand", friendly_name="Test Friendly Brand")
        self.size = Size.objects.create(
            eu_name="42", uk_name="8", us_m_name="S9", us_w_name="10")
        self.quality = Quality.objects.create(
            name="High Quality", description="Test description", rating=4)
        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            size=self.size,
            quality=self.quality,
            sku="TEST123",
            name="Test Product",
            description="Test Description",
            price=99.99,
            shoe_sex="male",
            sold=False
        )

        # Create a test client
        self.client = Client()

    def test_all_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sold_products_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('sold_products'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'home'))

    def test_product_detail_view(self):
        response = self.client.get(
            reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'home'))

    def test_edit_product_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(
            reverse('edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'home'))

    def test_delete_product_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(
            reverse('delete_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect

    def test_quality_view(self):
        response = self.client.get(reverse('quality'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/quality.html')


class FormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", friendly_name="Test Friendly Category")
        self.brand = Brand.objects.create(
            name="Test Brand", friendly_name="Test Friendly Brand")
        self.size = Size.objects.create(
            eu_name="EU42", uk_name="UK8", us_m_name="US9", us_w_name="US10")
        self.quality = Quality.objects.create(
            name="High Quality", description="Test description", rating=4)
        self.image = join(
            settings.BASE_DIR, "media/TEST.jpg")

    def test_product_form_valid(self):
        form_data = {
            'category': self.category.id,
            'brand': self.brand.id,
            'size': self.size.id,
            'quality': self.quality.id,
            'sku': 'TEST123',
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '99.99',
            'shoe_sex': 'male',
        }

        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_images_valid(self):
        form_data = {
            'category': self.category.id,
            'brand': self.brand.id,
            'size': self.size.id,
            'quality': self.quality.id,
            'sku': 'TEST123',
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '99.99',
            'shoe_sex': 'male',
        }

        # Prepare a list of SimpleUploadedFile for images
        images_data = [
            SimpleUploadedFile(self.image,
                               content=open("media/TEST.jpg", 'rb').read(), content_type="image/jpg"),
            SimpleUploadedFile(self.image,
                               content=open("media/TEST.jpg", 'rb').read(), content_type="image/jpg"),
        ]

        form = ProductForm(data=form_data, files={'images': images_data})

        self.assertTrue(form.is_valid(), f"Form is not valid: {form.errors}")

    def test_product_form_invalid(self):
        # Test form validation with missing required fields
        form_data = {
            # Remove the 'category' field to make the form invalid
            'brand': self.brand.id,
            'size': self.size.id,
            'quality': self.quality.id,
            'sku': 'TEST123',
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '99.99',
            'shoe_sex': 'male',
        }

        images_data = [
            SimpleUploadedFile("TEST.jpg",
                               content=open("TEST.jpg", 'rb').read(), content_type="image/jpg"),
            SimpleUploadedFile("media/TEST.jpg",
                               content=open("TEST.jpg", 'rb').read(), content_type="image/jpg"),
        ]

        form = ProductForm(data=form_data, files={'images': images_data})
        self.assertFalse(form.is_valid())

        self.assertIn('category', form.errors.keys())

    def test_product_form_images_invalid(self):
        # Test form validation with invalid image files
        form_data = {
            'category': self.category.id,
            'brand': self.brand.id,
            'size': self.size.id,
            'quality': self.quality.id,
            'sku': 'TEST123',
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '99.99',
            'shoe_sex': 'male',
        }

        # Invalid image file (not an image)
        with open("TEST.txt", "rb") as file:
            actual_content = file.read()

        invalid_images_data = [
            SimpleUploadedFile("TEST.txt",
                               actual_content, content_type="text/plain")
        ]

        form = ProductForm(data=form_data, files={
                           'images': invalid_images_data})

        self.assertFalse(form.is_valid())
        self.assertIn('images', form.errors.keys())

    def test_product_form_widget_attrs(self):
        form = ProductForm()
        for field_name, field in form.fields.items():
            self.assertIn('class', field.widget.attrs)
            self.assertEqual(
                field.widget.attrs['class'], 'border-black rounded-0')
