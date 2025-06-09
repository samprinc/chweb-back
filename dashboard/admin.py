from django.contrib import admin
from .models import SiteContent, Event, GalleryLink, Sermon, Book, ShopItem

admin.site.register(SiteContent)
admin.site.register(Event)
admin.site.register(GalleryLink)
admin.site.register(Sermon)
admin.site.register(Book)
admin.site.register(ShopItem)
