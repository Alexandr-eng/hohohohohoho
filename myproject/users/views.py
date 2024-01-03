from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .permissions import IsProviderUser, IsConsumerUser

from .models import User, Warehouse, Product, Basket
from .serializers import UserSerializer, BasketSerializer, WarehouseSerializer, \
    ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = UserSerializer

    authentication_classes = []
    permission_classes = []


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = WarehouseSerializer
    permission_classes = [IsProviderUser,]

    @action(detail=True, methods=["GET"])
    def products(self, request, pk=None):
        warehouse = self.get_object()
        products = Product.objects.filter(warehouse=warehouse)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = ProductSerializer
    permission_classes = [IsProviderUser,]


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = BasketSerializer
    permission_classes = [IsConsumerUser,]
