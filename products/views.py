from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product

def index(request):
    products = Product.objects.all().filter(is_published=True)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }
    return render(request,'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context ={
        'product': product
    }

    return render(request,'products/product.html', context)

def search(request):
    return render(request,'products/search.html')
