import pytest
from product.models import Product
from order.serializers import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_com_produto_inativo():
    # Cria dois produtos: um ativo e um inativo
    ativo = Product.objects.create(title="Ativo", price=100.0, active=True)
    inativo = Product.objects.create(title="Inativo", price=200.0, active=False)

    # Simula uma ordem com os dois produtos
    class OrderMock:
        def product(self):
            return Product.objects.filter(id__in=[ativo.id, inativo.id])

        product = property(product)

    order = OrderMock()

    # Serializa a ordem
    serializer = OrderSerializer(instance=order)
    data = serializer.data

    # Verifica se o total soma ambos os preços
    assert data["total"] == 300.0

    # Verifica se o produto inativo aparece e está marcado como tal
    assert any(prod["active"] is False for prod in data["product"])
