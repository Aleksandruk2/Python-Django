from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path("upload_temp_image/", views.upload_temp_image, name="upload_temp_image"),
]