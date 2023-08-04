from rest_framework import serializers
from apps.categories.models import Category
from apps.products.serializers import ProductSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    category_detail = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'category_detail']


class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'is_active', 'category_products']


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'image', 'is_active']