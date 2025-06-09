from rest_framework import viewsets
from .models import SiteContent, Event, GalleryLink, Sermon, Book, ShopItem
from .serializers import (
    SiteContentSerializer, EventSerializer, GalleryLinkSerializer,
    SermonSerializer, BookSerializer, ShopItemSerializer
)

class SiteContentViewSet(viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GalleryLinkViewSet(viewsets.ModelViewSet):
    queryset = GalleryLink.objects.all()
    serializer_class = GalleryLinkSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
