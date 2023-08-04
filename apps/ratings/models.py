from django.db import models
from apps.users.models import User
from apps.products.models import Product


class Rating(models.Model):
    RATING_CHOICES =(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rating}"


