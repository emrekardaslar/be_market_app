from rest_framework import viewsets
from .models import Product, Comment, Rating, Order, OrderItem

from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('created_at')
    serializer_class = RatingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by("created_at")
    serializer_class = OrderItemSerializer
