from .views import OrderViewSet, OrderItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemViewSet)

urlpatterns = router.urls
