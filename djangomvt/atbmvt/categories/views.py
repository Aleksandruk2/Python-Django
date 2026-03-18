from django.shortcuts import render, redirect
from .forms import CategoryCreateForm
from .utils import save_image
from .models import Category
from django.contrib import messages

# Create your views here.
def create_category(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                image = request.FILES.get("image")
                if image:
                    category.image = save_image(image, size=(600,600), folder="categories")
                category.save()
                return redirect('homepage')
            except Exception as e:
                messages.error(request, f"Щось пішло не так: {str(e)}")
    else:
        form = CategoryCreateForm()

    return render(request, "categories/create.html", {"form": form})

def categories_list(request):
    items = Category.objects.all()
    return render(request, 'categories/categories-list.html', {'items': items})