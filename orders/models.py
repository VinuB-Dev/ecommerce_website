from django.db import models
from datetime import datetime

class Order(models.Model):
    product = models.CharField(max_length=200)
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    user_id = models.IntegerField()
    def __str__(self):
        return self.name