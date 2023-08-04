from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category_image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name