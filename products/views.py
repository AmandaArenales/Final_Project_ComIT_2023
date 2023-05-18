import random, operator

from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from vendor.models import Vendor


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug = category_slug, slug = product_slug)

    title = product_slug.split('_')[0].capitalize()
    list_products =  Product.objects.filter(title=product).values()
    
    list_id = []
    list_price = []
    list_final = {}

    for p in list_products:
        list_id.append(p['vendor_id'])
        list_price.append(p['price'])

    vendor_name = []
    vendor_id =  Vendor.objects.filter(pk__in=list_id)
  
    for n in vendor_id:
        vendor_name.append(n.name)

    for p, v in enumerate(vendor_name):
        list_final[v] = list_price[p]

    list_final = dict(sorted(list_final.items(), key=operator.itemgetter(1)))
    print(list_final)

    other_products = list(product.category.products.exclude(id=product.id)) 

    if len(other_products) >= 3:
        other_products = random.sample(other_products, 3)

    template = 'product.html'
    content = {'product': product, 'other_products': other_products, 'list_final': list_final}

    return render(request, template, content)

def category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    template = 'category.html'
    content = {'category ': category}
    return render(request, template, content)

