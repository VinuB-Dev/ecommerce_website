from django.shortcuts import render
from .models import Seller
from products.choices import price_choices, seller_choices

def search(request):
    queryset_list1 = Seller.objects.all()


    if 'seller' in request.GET:
        name = request.GET['seller']
        if name:
            queryset_list1 = queryset_list1.filter(name__iexact=name)

    context = {
         'price_choices':price_choices,
        'seller_choices':seller_choices,
        'seller': queryset_list1
    }

    return render(request,'products/search.html', context)
