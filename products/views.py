import random 

from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug = category_slug, slug = product_slug)
    other_products = list(product.category.products.exclude(id=product.id)) 

    if len(other_products) >= 3:
        other_products = random.sample(other_products, 3)
    template = 'product.html'
    content = {'product': product, 'other_products': other_products}
    return render(request, template, content)

def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    template = 'category.html'
    content = {'category ': category}
    return render(request, template, content)

"""def price_by_vendor(request, slug_product):
    products = Product.obj
    for e in Product.objects.get(id = product.id):
        if (e.get_name() == slug_product):"""
