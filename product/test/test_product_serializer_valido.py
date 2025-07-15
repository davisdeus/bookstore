import pytest
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_valido():
    # Cria um produto válido no banco de dados com todos os campos obrigatórios preenchidos
    produto = Product.objects.create(
        title="Celular", description="Smartphone Android", price=1200, active=True
    )

    # Inicializa o serializer usando esse produto como instância
    serializer = ProductSerializer(instance=produto)

    # Gera o dicionário com os dados serializados
    data = serializer.data

    # Verifica se os campos principais foram serializados corretamente
    assert data["title"] == "Celular"
    assert data["description"] == "Smartphone Android"
    assert data["price"] == 1200
    assert data["active"] is True
