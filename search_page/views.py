from django.shortcuts import render
from products.models import Product

def search_page(request):
    newest_products =  Product.objects.all()
    context        = {'newest_products': newest_products}
    template       = 'search_page.html'
    print(newest_products)

    return render (request, template, context)
