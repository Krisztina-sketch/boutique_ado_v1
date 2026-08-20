from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        products = products.filter(category__id=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {
        'product': product,
    }

    return render(request, 'products/delete_product.html', context)