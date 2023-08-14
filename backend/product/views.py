from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated

from .models import Product, Comment, Rating, Order, OrderItem, FavoriteList, Category, Subcategory, Brand
from .pagination import StandardResultsSetPagination
from rest_framework import filters
from .serializers import ProductSerializer, CommentSerializer, RatingSerializer, OrderSerializer, OrderItemSerializer, \
    FavoriteListSerializer, FavoriteListProductsSerializer, SubcategorySerializer, \
    CategorySerializer, BrandSerializer
from .permissions import IsReadOnlyButStaff, IsReadOnlyButUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.db.models import Avg


class ProductViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsReadOnlyButStaff]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['id']
    search_fields = ['name', 'description', 'subcategory__name', 'subcategory__category__name', 'brand__name']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsReadOnlyButUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('created_at')
    serializer_class = RatingSerializer
    permission_classes = [IsReadOnlyButUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id']

    def list(self, request, *args, **kwargs):
        product_id = request.query_params.get("product_id")
        if request.data.get("user") is None:
            user = request.user.id
        else:
            user = request.data.get("user")

        avg_rating = self.queryset.filter(product_id=product_id).aggregate(Avg('value'))
        if user is not None:
            rating_id = self.queryset.filter(product_id=product_id, user_id=user).first().id
            return Response({'results': {"avg_rating": avg_rating["value__avg"], "rating_id": rating_id}})

        return Response({'results': {"avg_rating": avg_rating["value__avg"]}})

    def update(self, request, *args, **kwargs):
        product_id = request.data.get("product")
        value = request.data.get("value")
        if request.data.get("user") is None:
            user_id = request.user.id
            request.data['user'] = user_id
        else:
            user_id = request.data.get("user")

        instance = self.queryset.get(product_id=product_id, user_id=user_id)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(status=200)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by("created_at")
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if 'user_id' not in self.request.query_params:
            orders = Order.objects.filter(user_id=user.id)
            self.queryset = self.queryset.filter(order__in=orders)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product")
        quantity = request.data.get("quantity")
        order_id = request.data.get("order")
        order = Order.objects.get(id=order_id)
        product = Product.objects.get(id=product_id)
        if request.data.get("user") is None:
            user = request.user
        else:
            user = request.data.get("user")

        order_item = OrderItem(quantity=quantity, order=order, product=product)
        order_item.save()
        return Response(status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.order.user != request.user:
            return Response({"error": "You don't have permission to remove this order item"},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)

        # Check if the order has any remaining items
        remaining_order_items = OrderItem.objects.filter(order=instance.order)
        if not remaining_order_items.exists():
            instance.order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# class CategoryNamesViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()  # TODO: Product.objects.values_list('category', flat=True).order_by('category').distinct()
#     serializer_class = CategoryNameSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FavoriteListViewSet(viewsets.ModelViewSet):
    queryset = FavoriteList.objects.all()

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

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product")
        product = Product.objects.get(id=product_id)
        if request.data.get("user") is None:
            user = request.user
        else:
            user = request.data.get("user")
        favorite_list = FavoriteList(user=user, product=product)
        favorite_list.save()
        return Response(status=200)

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteListProductsSerializer
        return FavoriteListSerializer

    def get_queryset(self):
        user = self.request.user
        if 'user_id' not in self.request.query_params:
            self.queryset = self.queryset.filter(user=user)
        return self.queryset
