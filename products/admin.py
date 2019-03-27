from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price','seller')
    list_display_links = ('id', 'title')
    list_filter = ('seller',)
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
