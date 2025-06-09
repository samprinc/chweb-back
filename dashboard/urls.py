from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SiteContentViewSet, EventViewSet, GalleryLinkViewSet,
    SermonViewSet, BookViewSet, ShopItemViewSet
)

router = DefaultRouter()
router.register(r'site-content', SiteContentViewSet)
router.register(r'events', EventViewSet)
router.register(r'gallery-links', GalleryLinkViewSet)
router.register(r'sermons', SermonViewSet)
router.register(r'books', BookViewSet)
router.register(r'shop-items', ShopItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
