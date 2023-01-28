from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product, Comment, Rating, Order, OrderItem, FavoriteList


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class CategoryNameSerializer(ModelSerializer):
    # category = serializers.CharField()
    class Meta:
        model = Product
        fields = [
            'category'
        ]


class FavoriteListProductsSerializer(ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteList
        fields = "__all__"

    def get_product(self, obj):
        products = Product.objects.filter(id=obj.product_id)
        serializer = ProductSerializer(products, many=True, context=self.context)
        return serializer.data


class FavoriteListSerializer(ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = "__all__"
