from django import forms
from .models import Category

class CategoryCreateForm(forms.ModelForm):

    name = forms.CharField(
        label="Назва категорії",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть назву категорії",
            "id": "name",
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
    slug = forms.CharField(
        label="Slug",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть slug",
            "id": "slug",
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
        fields = ["name", "slug", "description", "image"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Назва повинна містити мінімум 3 символи")
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("Категорія вже існує")
        return name
    
    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        if len(slug) < 3:
            raise forms.ValidationError("Slug повинен містити мінімум 3 символи")
        if Category.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Такий slug вже існує")
        return slug