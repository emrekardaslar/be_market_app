from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated

from .models import Product, Comment, Rating, Order, OrderItem, FavoriteList
from .pagination import StandardResultsSetPagination
from rest_framework import filters
from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer, \
    CategoryNameSerializer, FavoriteListSerializer
from .permissions import IsReadOnlyButStaff, IsReadOnlyButUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


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
    queryset = Product.objects.all()  # TODO: Product.objects.values_list('category', flat=True).order_by('category').distinct()
    serializer_class = CategoryNameSerializer


class FavoriteListViewSet(viewsets.ModelViewSet):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if 'user_id' in self.request.query_params:
            user_id = self.request.query_params['user_id']
            if user_id != str(user.id):
                return Response({"error": "You do not have permission to view this user's favorites."}, status=401)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        if 'user_id' not in self.request.query_params:
            self.queryset = self.queryset.filter(user=user)
        return self.queryset
