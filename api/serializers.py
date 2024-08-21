from rest_framework import serializers
from foodano import models


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


# ==========================================================================
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email']

# ==========================================================================

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Info
        fields = '__all__'


class ProductEnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
    

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'