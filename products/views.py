from django.shortcuts import render, redirect
from products.models import Product
from accounts.models import Account


def show_product(request):
    try:
        products = Product.objects.filter(quantity__gte=1).filter(store__status='C')
        context = {'products': products}
        return render(request, 'product.html', context)
    except:
        return render(request, 'product.html')
