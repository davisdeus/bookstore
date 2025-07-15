import pytest
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_invalido_sem_titulo():
    # Define dados incompletos: falta o campo obrigatório 'title'
    invalid_data = {"description": "Produto sem nome", "price": 500, "active": True}

    # Tenta criar um serializer com os dados inválidos
    serializer = ProductSerializer(data=invalid_data)

    # O serializer deve considerar os dados inválidos
    assert not serializer.is_valid()

    # O erro deve estar associado ao campo 'title' que está faltando
    assert "title" in serializer.errors
