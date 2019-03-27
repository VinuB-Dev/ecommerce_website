from django.db import models
from datetime import datetime
from sellers.models import Seller

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    is_published = models.BooleanField(default='True')
    def __str__(self):
        return self.title
