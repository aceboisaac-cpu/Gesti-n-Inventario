from decimal import Decimal

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "category"]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del producto'
            }),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < Decimal("0.01"):
            raise forms.ValidationError("El precio debe ser al menos 0.01.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock
