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
    permission_classes = [IsProviderUser]

    @action(detail=True)
    def products(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        free_product = warehouse.products.filter(baskets__isnull=True)
        return Response(ProductSerializer(free_product, many=True).data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = ProductSerializer
    permission_classes = [IsProviderUser]


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = BasketSerializer
    permission_classes = [IsConsumerUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied(
                'У вас нет разрешения на удаление этой корзины')
