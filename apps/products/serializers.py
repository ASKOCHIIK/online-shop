from rest_framework import serializers
from apps.products.models import Product
from apps.categories.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'quantity', 'price', 'rating', 'country', 'created_at', 'category', 'category_name', 'owner_email']


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'quantity', 'price', 'country', 'created_at', 'category', 'owner']


class ProductUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150, required=False)
    description = serializers.CharField(max_length=10000, required=False)
    image = serializers.ImageField(use_url=True, allow_empty_file=True, required=False)
    quantity = serializers.IntegerField(required=False)
    price = serializers.IntegerField(required=False)
    country = serializers.CharField(max_length=50, required=False)
    created_at = serializers.CharField(max_length=20, required=False)
    category = serializers.PrimaryKeyRelatedField(required=False, queryset=Category.objects.all())

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.country = validated_data.get('country', instance.country)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


