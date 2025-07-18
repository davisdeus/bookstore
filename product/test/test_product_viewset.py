import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models.product import Product


class TestProductViewSet(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    
    def test_get_all_products(self):
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        products = json.loads(response.content)
        self.assertEqual(products[0]["title"], self.product.title)
        self.assertEqual(products[0]["price"], self.product.price)
        self.assertEqual(products[0]["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'new product',
            'price': 150.00,
            'categories_id': [category.id]
        })

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(title='new product')

        self.assertEqual(created_product.title, 'new product')
        self.assertEqual(created_product.price, 150.00)