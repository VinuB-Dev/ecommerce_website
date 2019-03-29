from django.shortcuts import render
from django.http import HttpResponse
from products.choices import price_choices, seller_choices

from products.models import Product
from sellers.models import Seller

def index(request):
    products = Product.objects.all().filter(is_published=True)[:3]

    context = {
        'products': products,
        'price_choices':price_choices,
        'seller_choices':seller_choices
    }

    return render(request,'pages/index.html', context)


def about(request):
    # Get all sellers
    sellers = Seller.objects.all()

    context = {
        'sellers': sellers
    }
    return render(request,'pages/about.html', context)

