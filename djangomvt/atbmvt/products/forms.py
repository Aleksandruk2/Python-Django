from django import forms

from .models import Category
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label="Категорія",
        queryset=Category.objects.all(),
        empty_label="Виберіть категорію",
    )
    name = forms.CharField(
        label="Назва продукту",
        widget=forms.TextInput(attrs={
            "placeholder": "Введіть назву категорії",
            "id": "name",
        })
    )
    slug = forms.CharField(
        label="Slug",
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Введіть slug",
            "id": "slug",
        })
    )
    description = forms.CharField(
        label="Опис",
        required=False,
        widget=forms.Textarea(attrs={
            "rows": 4
        })
    )
    price = forms.DecimalField(
        label="Ціна",
        required=True,
        widget=forms.NumberInput({})
    )

    class Meta:
        model = Product
        fields = ["category", "name", "slug", "description", "price"]

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image", "priority"]   # або ["image", "is_main"] якщо ти вибрав boolean