from rest_framework import viewsets, permissions, generics
from .models import Product, Comment, Rating, Order, OrderItem
from .pagination import StandardResultsSetPagination
from rest_framework import filters
from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer
from .permissions import IsReadOnlyButStaff, IsReadOnlyButUser
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsReadOnlyButStaff]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory']
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
