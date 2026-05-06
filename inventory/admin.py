from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columnas que queremos ver en la lista
    list_display = ("name", "category", "price", "stock")

    # Buscador por nombre y categoría
    search_fields = ("name", "category")

    # Filtros laterales
    list_filter = ("category",)
