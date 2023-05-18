from django.core.files import File
from django.db import models

#from decimal import Decimal

from io import BytesIO
from PIL import Image
from vendor.models import Vendor

# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length = 200)
    slug        = models.SlugField(max_length = 200) #used in the urls
    ordering    = models.IntegerField(default = 0)
    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title
    
class Product(models.Model):
    category    = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)
    vendor      = models.ForeignKey(Vendor, related_name = 'products', on_delete = models.CASCADE)
    title       = models.CharField(max_length = 200)
    slug        = models.SlugField(max_length = 200, unique = True) #used in the urls
    price       = models.DecimalField(max_digits = 6, decimal_places = 2, blank=True, default = 0.0)
    date_added  = models.DateTimeField(auto_now_add = True)
    image       = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail   = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    class Meta:
        ordering = ['-date_added'] #data in descent order
    
    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
        
    def make_thumbnail(self, image, size = (290, 200)):
        img = Image.open(image) #create a image object
        img.convert('RGB')
        img.thumbnail(size) #PIL built in function 

        thumb_io = BytesIO() #create a instance of it
        img.save(thumb_io, 'JPEG', quality = 85)

        thumbnail = File(thumb_io, name = image.name) #create a file before it save on function get_thumbnail
        return thumbnail

