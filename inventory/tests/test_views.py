import pytest
from django.urls import reverse

from inventory.models import Product


@pytest.mark.django_db
def test_product_list_view(client):
    """Verifica que la página principal cargue y use el template correcto"""
    # Creamos un producto de prueba
    Product.objects.create(name="Producto Test", price=10, stock=5, category="Test")

    # Hacemos una petición GET a la lista
    url = reverse("product_list")
    response = client.get(url)

    assert response.status_code == 200
    assert "Producto Test" in response.content.decode()
    assert "inventory/product_list.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_product_search_view(client):
    """Verifica que el buscador funcione correctamente"""
    Product.objects.create(name="Laptop", price=100, stock=5, category="PC")
    Product.objects.create(name="Mouse", price=20, stock=10, category="PC")

    # Buscamos "Laptop"
    url = reverse("product_list")
    response = client.get(url, {"q": "Laptop"})

    assert "Laptop" in response.content.decode()
    assert "Mouse" not in response.content.decode()


@pytest.mark.django_db
def test_product_create_view(client):
    """Verifica que se pueda crear un producto vía POST"""
    url = reverse("product_create")
    data = {"name": "Nuevo Teclado", "price": "45.00", "stock": "20", "category": "Periféricos"}

    # Enviamos el formulario
    response = client.post(url, data)

    # 302 significa que redirigió (éxito)
    assert response.status_code == 302
    assert Product.objects.filter(name="Nuevo Teclado").exists()


@pytest.mark.django_db
def test_product_delete_view(client):
    """Verifica que se pueda borrar un producto"""
    p = Product.objects.create(name="Borrar", price=10, stock=5, category="X")
    url = reverse("product_delete", args=[p.pk])

    # El borrado en Django suele ser un POST de confirmación
    response = client.post(url)

    assert response.status_code == 302
    assert not Product.objects.filter(name="Borrar").exists()
