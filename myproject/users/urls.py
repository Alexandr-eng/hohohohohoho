from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('warehouse', WarehouseViewSet)
router.register('products', ProductViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)