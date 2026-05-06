import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from inventory.models import Product

# --- TESTS DE CAMINO FELIZ (DATOS CORRECTOS) ---

@pytest.mark.django_db
def test_product_creation_is_valid():
    """Valida que un producto con datos correctos se cree y represente bien"""
    product = Product.objects.create(
        name="Monitor 4K",
        price=500.00,
        stock=5,
        category="Hardware"
    )
    assert product.pk is not None
    assert str(product) == "Monitor 4K"
    # Verificamos que no tire error al validar
    product.full_clean() 


# --- TESTS DE VALIDACIÓN DE CAMPOS (PUNTOS DE FALLO) ---

@pytest.mark.django_db
@pytest.mark.parametrize("name, price, stock, category", [
    ("", Decimal("100.00"), 10, "Tech"),          # Nombre vacío
    ("Producto", Decimal("-1.00"), 10, "Tech"),   # Precio negativo
    ("Producto", Decimal("0.00"), 10, "Tech"),    # Precio cero (el validador pide min 0.01)
    ("Producto", Decimal("100.00"), -5, "Tech"),  # Stock negativo
    ("A"*256, Decimal("100.00"), 10, "Tech"),     # Nombre demasiado largo (>255)
    ("Producto", Decimal("100.00"), 10, ""),      # Categoría vacía
])
def test_product_invalid_data_raises_error(name, price, stock, category):
    """
    Este test es un tanque: prueba múltiples fallos de una.
    Cualquier dato incorrecto DEBE lanzar una ValidationError.
    """
    product = Product(
        name=name,
        price=price,
        stock=stock,
        category=category
    )
    with pytest.raises(ValidationError):
        product.full_clean()

# --- TESTS DE LÍMITES (EDGE CASES) ---

@pytest.mark.django_db
def test_product_boundary_values():
    """Probamos los límites exactos de los validadores"""
    # Precio mínimo permitido (0.01)
    product_min_price = Product(name="Test", price=Decimal("0.01"), stock=0, category="Test")
    product_min_price.full_clean() # No debería fallar

    # Stock mínimo permitido (0)
    product_min_stock = Product(name="Test", price=Decimal("10.00"), stock=0, category="Test")
    product_min_stock.full_clean() # No debería fallar
