from django.test import TestCase
from django.test.client import Client
from mainapp.models import ProductCategory, Product


# Create your tests here.
class MainAppSmokeTest(TestCase):
    status_code_success = 200

    def setUp(self):
        category = ProductCategory.objects.create(
            name='cat1'
        )
        for i in range(10):
            Product.objects.create(
                category=category,
                name=f'prod{i}',
            )

        self.client = Client()

    def test_main_app_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
