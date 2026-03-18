from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("create/", views.create_category, name="create"),
    path("categories-list/", views.categories_list, name="categories_list"),
]