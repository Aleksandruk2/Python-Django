from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import ProductImage
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import JsonResponse
import uuid

# Create your views here.

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        images_ids = request.POST.getlist('images')
        if form.is_valid():
            product = form.save()

            for idx, img_id in enumerate(images_ids):
                img = ProductImage.objects.get(id=img_id)
                img.product = product
                img.priority = idx
                img.save()

            return redirect("products:create")  # назва URL на список товарів
    else:
        form = ProductForm()

    return render(request, "products/create.html", {"form": form})

@csrf_exempt
def upload_temp_image(request):
    if request.method == "POST":
        file_key = list(request.FILES.keys())[0]
        image_file = request.FILES[file_key]

        img = ProductImage()
        img_image = Image.open(image_file)
        if img_image.mode in ("RGBA", "P"):
            img_image = img_image.convert("RGB")

        filename = f"{uuid.uuid4().hex}.webp"
        buffer = BytesIO()
        img_image.save(buffer, format="WEBP")
        buffer.seek(0)
        img.image.save(filename, ContentFile(buffer.read()), save=True)
        
        return JsonResponse({"file_id": img.id})