from rest_framework import serializers

from product.models import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, many=True)

    class Meta:
        models = Product
        fields = [
            "id",
            "title",
            "description",
            "prince",
            "active",
            "category",
        ]
