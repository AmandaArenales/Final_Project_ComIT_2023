from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.text import slugify #convert the title into a slug

from products.models import Product
from .models import Vendor

from .forms import ProductForm

#sign up for the vendor
def become_vendor(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            login(request, user)
            Vendor.objects.create(name = user.username, created_by = user)
            return redirect('vendor_admin')   
    else:
        form = UserCreationForm() 
    context = {'form': form}
    template = 'become_vendor.html'
    return render(request, template, context)

#vendor_login using the login decoretor
@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    print(vendor.name)
    products = vendor.products.all()
    context = {'vendor': vendor, 'products': products}
    template = 'vendor_admin.html'
    return render (request, template, context)

@login_required  
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) #requeste.FILES because the files will be submitted.

        if form.is_valid():
            product = form.save(commit = False) #false is because the vendor isn't set yet and it will not be commited to the database now.
            product.vendor = request.user.vendor #now it has a vendor
            product.slug = slugify(product.title)
            product.save() #it will be saved in the database

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    context = {'form': form}
    template = 'add_product.html'
    return render(request, template, context)

    


 
