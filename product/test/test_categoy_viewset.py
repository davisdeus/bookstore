import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from product.factories import CategoryFactory
from product.models.product import Category


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="Electronics")
        # self.product = ProductFactory(
        #     title="pro controller",
        #     price=200.00,
        # )

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        self.assertEqual(category_data["results"][0]["title"], self.category.title)
        # self.assertEqual(product_data[0]["price"], self.product.price)
        # self.assertEqual(product_data[0]["active"], self.product.active)

    def test_create_category(self):
        data = json.dumps({"title": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # import pdb; pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

        self.assertEqual(created_category.title, "technology")
