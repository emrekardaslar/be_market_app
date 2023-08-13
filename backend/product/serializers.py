from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product, Comment, Rating, Order, OrderItem, FavoriteList, Category, Subcategory, Brand


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_subcategories(self, obj):
        return [subcategory.name for subcategory in obj.subcategory_set.all()]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category_name = serializers.SerializerMethodField()
    subcategory_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.subcategory.category.name if obj.subcategory else None

    def get_subcategory_name(self, obj):
        return obj.subcategory.name if obj.subcategory else None

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')  # Use 'orderitem_set' as the source

    class Meta:
        model = Order
        fields = "__all__"


# class CategoryNameSerializer(ModelSerializer):
#     # category = serializers.CharField()
#     class Meta:
#         model = Product
#         fields = [
#             'category'
#         ]


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
