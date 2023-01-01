from django.urls import path, include

from .views import ProductViewSet, CommentViewSet, RatingViewSet, OrderViewSet, OrderItemViewSet, CategoryNamesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemViewSet)
router.register(r'categoryNames', CategoryNamesViewSet)

urlpatterns = router.urls
