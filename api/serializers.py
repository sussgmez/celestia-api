from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, ProductImage, ProductSize, ProductVariant, Order, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "category", "price", "created_at"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "productvariant", "image"]


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["id", "productvariant", "size", "stock"]


class ProductVariantSerializer(serializers.ModelSerializer):
    productimages = ProductImageSerializer(many=True)
    productsizes = ProductSizeSerializer(many=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductVariant
        fields = ["id", "product", "color", "discount", "productimages", "productsizes"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "productsize", "user", "quantity"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "subcategory_of"]
