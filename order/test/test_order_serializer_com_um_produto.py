import pytest
from product.models import Product
from order.serializers import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_com_um_produto():
    # Cria um produto no banco
    produto = Product.objects.create(title="Produto Único", price=123.45)

    # Simula uma ordem contendo esse produto
    class OrderMock:
        def product(self):
            return Product.objects.filter(id=produto.id)

        product = property(product)

    order = OrderMock()

    # Serializa a ordem
    serializer = OrderSerializer(instance=order)
    data = serializer.data

    # Verifica se o total corresponde ao preço do produto
    assert data["total"] == 123.45

    # Confere se a lista contém 1 item e se os dados batem
    assert len(data["product"]) == 1
    assert data["product"][0]["title"] == "Produto Único"
