import pytest
from product.models import Product
from order.serializers import (
    OrderSerializer,
)  # ajuste conforme o local do seu serializer


# Marca o teste para acessar o banco de dados de forma segura com pytest
@pytest.mark.django_db
def test_order_serializer_total_calculado():
    # Criação de dois produtos no banco de dados para simular uma ordem
    produto1 = Product.objects.create(title="Produto A", price=100.0)
    produto2 = Product.objects.create(title="Produto B", price=50.0)

    # Mock de uma classe Order (caso não tenha um modelo real ainda)
    # O método product retorna um queryset contendo os dois produtos criados
    class OrderMock:
        def product(self):
            return Product.objects.filter(id__in=[produto1.id, produto2.id])

        product = property(product)

    # Instancia o mock da ordem
    order = OrderMock()

    # Inicializa o serializer com a instância da ordem
    serializer = OrderSerializer(instance=order)

    # Obtém os dados serializados
    data = serializer.data

    # Verifica se os campos esperados estão presentes na saída do serializer
    assert "product" in data
    assert "total" in data

    # Verifica se o campo `total` foi calculado corretamente (100 + 50)
    assert data["total"] == 150.0

    # Verifica se o campo `product` retornou os dois itens esperados
    assert len(data["product"]) == 2

    # Confere os dados dos produtos serializados
    assert data["product"][0]["title"] == "Produto A"
    assert data["product"][1]["price"] == 50.0
