from rest_framework import serializers
from market.models import Product, Category, Reviews, Basket


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price", "marks", "category")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class AddReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('text', 'user', 'product',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("product", "count", "price", "user",)
