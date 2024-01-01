from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import User, Warehouse, Product, Basket
from .serializers import UserSerializer, BasketSerializer, WarehouseSerializer, ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = UserSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = WarehouseSerializer

    @action(detail=True)
    def products(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        free_product = warehouse.products.filter(baskets__isnull=True)
        return Response(ProductSerializer(free_product, many=True).data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = ProductSerializer


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = BasketSerializer