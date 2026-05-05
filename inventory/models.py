from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    # El nombre no puede estar vacío (Django lo hace por defecto si no ponés blank=True)
    name = models.CharField(max_length=255, verbose_name="Nombre")
    
    # El precio debe ser un número mayor a cero
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio"
    )
    
    # El stock no puede ser negativo
    stock = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Cantidad en Stock"
    )
    
    category = models.CharField(max_length=100, verbose_name="Categoría")

    # Esto es para que en el panel de Django veamos el nombre del producto, no "Product object (1)"
    def __str__(self):
        return self.name

    # Metadatos para que el Admin hable en español
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

