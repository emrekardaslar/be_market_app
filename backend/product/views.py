from django.http import JsonResponse
from requests import Response
from rest_framework import viewsets, permissions, generics, status
from .models import Product, Comment, Rating, Order, OrderItem
from .pagination import StandardResultsSetPagination
from rest_framework import filters
from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer, \
    CategoryNameSerializer
from .permissions import IsReadOnlyButStaff, IsReadOnlyButUser
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Value, CharField


class ProductViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsReadOnlyButStaff]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'category', 'subcategory']
    ordering_fields = '__all__'
    ordering = ['name']
    search_fields = ('name', 'category')


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


class CategoryNamesViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()# TODO: Product.objects.values_list('category', flat=True).order_by('category').distinct()
    serializer_class = CategoryNameSerializer

