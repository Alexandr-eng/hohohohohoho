from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_groups_set')
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='user_permissions_set')
    TYPES = (
        ('P', 'Поставщик'),
        ('C', 'Потребитель'),
    )
    type = models.CharField(max_length=1, choices=TYPES, default='C')

    def __str__(self):
        return self.username


class Warehouse(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='baskets', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Basket for {self.user.username} : Product {self.product.name}'