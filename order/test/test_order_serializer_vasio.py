import pytest
from product.models import Product
from order.serializers import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_vazio():
    # Retorna um queryset vazio com o mesmo tipo que o .all() real
    vazio = Product.objects.none()

    class OrderMock:
        def product(self):
            return vazio

        product = property(product)

    order = OrderMock()
    serializer = OrderSerializer(instance=order)
    data = serializer.data

    # Verificações
    assert data["total"] == 0
    assert data["product"] == []
