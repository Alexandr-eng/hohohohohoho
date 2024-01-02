from rest_framework import serializers
from .models import User, Warehouse, Product, Basket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'password']
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            type=validated_data['type'],
        )

        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name']
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'warehouse', 'quantity']
        extra_kwargs = {"id": {"read_only": True}}


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}, "user": {"read_only": True}}