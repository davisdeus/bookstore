import pytest
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_com_categoria():
    # Cria duas categorias no banco
    cat1 = Category.objects.create(title="Eletrônicos", slug="eletronicos")
    cat2 = Category.objects.create(title="Ofertas", slug="ofertas")


    # Cria um produto e associa essas categorias usando ManyToMany
    produto = Product.objects.create(
        title="Notebook", description="Ultrabook leve", price=3500, active=True
    )
    produto.category.set([cat1, cat2])  # Associa as categorias ao produto

    # Inicializa o serializer com essa instância de produto
    serializer = ProductSerializer(instance=produto)

    # Obtém os dados serializados
    data = serializer.data

    # Verifica se o campo 'category' está presente na saída
    assert "category" in data

    # Garante que existem 2 categorias associadas
    assert len(data["category"]) == 2

    # Extrai os nomes das categorias serializadas
    nomes = [c["title"] for c in data["category"]]

    # Confirma que as categorias estão corretamente associadas
    assert "Eletrônicos" in nomes
    assert "Ofertas" in nomes
