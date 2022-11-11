from rest_framework.serializers import ModelSerializer
from .models import Product, Comment, Rating


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
