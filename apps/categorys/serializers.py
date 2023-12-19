from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    image = serializers.SerializerMethodField()

    def get_image(self, category):
        return category.image.url if category.image else None


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    image = serializers.SerializerMethodField()

    def get_image(self, category):
        return category.image.url if category.image else None
