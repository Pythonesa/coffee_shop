from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from products.forms import ProductForm
from products.models import Product


class ProductFormView(FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("all_products")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductsView(ListView):
    model = Product
    queryset = Product.objects.all()
    context_object_name = "products"
    template_name = "products/all_products.html"
