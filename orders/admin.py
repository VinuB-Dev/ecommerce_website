from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product','quantity','price','total_price')
    list_display_links =('id', 'product','quantity','price','total_price')
    search_fields =('product','')
    list_per_page = 25

admin.site.register(Order, OrderAdmin)
