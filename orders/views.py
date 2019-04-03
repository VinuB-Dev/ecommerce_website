from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order

def order(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        quantity = request.POST['quantity']
        user_id = request.POST['user_id']

        order = Order(product=product, product_id=product_id,name=name,
        quantity=quantity,user_id=user_id)

        order.save()

        messages.success(request, 'the product has been added to the cart')
        return redirect('/products/'+product_id)