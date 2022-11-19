from .views import ProductViewSet, CommentViewSet, RatingViewSet, OrderViewSet, OrderItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemViewSet)

urlpatterns = router.urls
