import pytest
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_descricao_opcional():
    # Cria um produto sem descrição
    produto = Product.objects.create(
        title="Produto sem descrição", price=150, active=True
    )

    # Serializa o produto
    serializer = ProductSerializer(instance=produto)
    data = serializer.data

    # Verifica se os campos obrigatórios estão corretos e se description é nulo ou ausente
    assert data["title"] == "Produto sem descrição"
    assert data["price"] == 150
    assert "description" in data
