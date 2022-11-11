from rest_framework import viewsets
from .models import Product, Comment, Rating

from .serializers import ProductSerializer, CommentSerializer, RatingSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('created_at')
    serializer_class = RatingSerializer
