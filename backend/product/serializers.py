from abc import ABC

from rest_framework.serializers import ModelSerializer
from .models import Product, Comment, Rating, Order, OrderItem
from rest_framework import serializers


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
