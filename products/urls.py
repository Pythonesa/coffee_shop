from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductFormView, ProductsView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("", ProductsView.as_view(), name="all_products"),
]
