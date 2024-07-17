from django.urls import path

from .views import ProductFormView, ProductsView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("", ProductsView.as_view(), name="all_products"),
]
