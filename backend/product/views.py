from rest_framework import viewsets, permissions
from .models import Product, Comment, Rating, Order, OrderItem

from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer
from .permissions import IsReadOnlyButStaff, IsReadOnlyButUser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [IsReadOnlyButStaff]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsReadOnlyButUser]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('created_at')
    serializer_class = RatingSerializer
    permission_classes = [IsReadOnlyButUser]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by("created_at")
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
