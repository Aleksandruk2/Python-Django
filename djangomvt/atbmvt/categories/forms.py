from django import forms
from .models import Category

class CategoryCreateForm(forms.ModelForm):

    name = forms.CharField(
        label="Назва категорії",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть назву категорії"
        })
    )
    description = forms.CharField(
        label="Опис",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4
        })
    )
    image = forms.ImageField(
        label="Зображення",
        required=False,
        widget=forms.FileInput(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = Category
        fields = ["name", "description", "image"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Назва повинна містити мінімум 3 символи")
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("Категорія вже існує")
        return name