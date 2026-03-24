from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.show_products, name='show-products'),
    path('create/', views.product_create, name='create'),
    path("edit/<int:product_id>/", views.product_edit, name="edit"),
    path("upload_temp_image/", views.upload_temp_image, name="upload_temp_image"),
    path("delete_temp_image/", views.delete_temp_image, name="delete_temp_image"),
    path('delete/<int:product_id>/', views.product_delete, name='delete'),
]