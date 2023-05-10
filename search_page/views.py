from django.shortcuts import render
from products.models import Product
from vendor.models import Vendor

def search_page(request):
    list_products =  Product.objects.all()

    list_title = []
    list_ids = []
    for p in list_products:
        if p.title not in list_title:
            list_ids.append(p.id)
            list_title.append(p.title)

    products_distinct =  Product.objects.filter(pk__in=list_ids)
    print(products_distinct)

    context        = {'products_distinct': products_distinct}
    template       = 'search_page.html'

    return render (request, template, context)





