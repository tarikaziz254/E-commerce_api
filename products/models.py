from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

