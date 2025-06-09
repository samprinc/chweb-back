from rest_framework import serializers
from .models import SiteContent, Event, GalleryLink, Sermon, Book, ShopItem

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta: model = SiteContent; fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta: model = Event; fields = '__all__'

class GalleryLinkSerializer(serializers.ModelSerializer):
    class Meta: model = GalleryLink; fields = '__all__'

class SermonSerializer(serializers.ModelSerializer):
    class Meta: model = Sermon; fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta: model = Book; fields = '__all__'

class ShopItemSerializer(serializers.ModelSerializer):
    class Meta: model = ShopItem; fields = '__all__'
