from django.urls import path, include

from .views import ProductViewSet, CommentViewSet, RatingViewSet, OrderViewSet, OrderItemViewSet, FavoriteListViewSet, \
    CategoryViewSet, SubcategoryViewSet, BrandViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemViewSet)
router.register(r'favoriteList', FavoriteListViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubcategoryViewSet)
router.register(r'brand', BrandViewSet)
urlpatterns = router.urls
