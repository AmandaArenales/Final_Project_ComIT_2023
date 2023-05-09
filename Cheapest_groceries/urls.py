"""Cheapest_groceries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings #for dynamic images
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

#own urls
from accounts.views import (
    login_view, 
    logout_view,
    register_view,
    test_view
)
from pages.views import (
    home_view, 
    contact_view
)

from products.views import (
    product,
    category
)


from search_page.views import (
   search_page
)

from vendor.views import (
    become_vendor, 
    vendor_admin,
    add_product
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/', add_product, name = 'add_product'), #own
    path('become_vendor/', become_vendor, name = 'become_vendor'), #own
    path('vendor_admin/', vendor_admin, name = 'vendor_admin'), #own
    path('search_page/', search_page, name = 'search_page'), #ownwn
    path('', home_view, name = 'home'), #own
    path('contact/', contact_view), #own
    path ('login/', login_view, name = 'login'), #own
    path('logout/', logout_view, name = 'logout'), #own
    path('register/', register_view, name = 'register'), #own
    path('test/', test_view), #own
    path('<slug:category_slug>/', category, name = 'category'), #own
    path('<slug:category_slug>/<slug:product_slug>/', product, name = 'product'), #own
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
