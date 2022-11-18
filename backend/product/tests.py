from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Selpak",
            price=5.99,
            imgLink="http://link",
            category="Mendil",
            subcategory="Mendil",
            description="Selpak mendil"
        )

    def test_product(self):
        selpak = Product.objects.get(name="Selpak")
        self.assertEqual(selpak.price, 5.99)
