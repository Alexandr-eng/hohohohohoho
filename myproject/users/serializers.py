from rest_framework import serializers
from .models import User, Warehouse, Product, Basket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'type']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'warehouse', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"