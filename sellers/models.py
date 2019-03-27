from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='photos/%Y/%m/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    reliable = models.BooleanField(default=False)
    def __str__(self):
        return self.name
