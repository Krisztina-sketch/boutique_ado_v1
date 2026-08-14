from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)