from .views import ProductViewSet, CommentViewSet, RatingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)
router.register(r'rating', RatingViewSet)

urlpatterns = router.urls
