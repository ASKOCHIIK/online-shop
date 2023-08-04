from django.db import models
from apps.products.models import Product
from apps.users.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_carts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_carts')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product}-{self.user}"

