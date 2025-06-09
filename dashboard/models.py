from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class SiteContent(models.Model):
    welcome_text = models.TextField(default="")
    def __str__(self): return "Welcome Message"

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    def __str__(self): return self.name

class GalleryLink(models.Model):
    url = models.URLField()
    def __str__(self): return self.url

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/')
    added_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self): return self.title


# models.py

class ShopItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True)

    def __str__(self):
        return self.name
