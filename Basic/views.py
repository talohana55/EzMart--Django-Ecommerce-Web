from django.shortcuts import render, redirect
from products.models import Product
from django.http import HttpResponse, Http404
from .models import Form
from django.contrib import messages
from django.views.generic.list import ListView
from orders.models import OrderedItem
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def index(request):
    allProducts = Product.objects.filter(quantity__gte=1).filter(store__status='C')
    products = {'allProducts':allProducts}
    return render(request, 'index.html', products)

def aboutUs(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'privacy.html')
def regulations(request):
    return render(request, 'regulations.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_form = Form(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        new_form.save()
        messages.info(request, 'Your message successfully sent')
        return redirect('contact')
    else:
        return render(request, 'contact.html')


class SearchProdView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchProdView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Product.objects.filter(quantity__gte=1).filter(store__status='C').filter(title__contains=query)
          result = postresult
       else: 
            result = Product.objects.filter(quantity__gte=1).filter(store__status='C')
       return result

@login_required(login_url='login')
def purchase (request):
    try:
        if request.method == 'POST':
            prod_id = request.POST['buy-id-btn']
            product = Product.objects.get(id = prod_id)
        return render(request, 'purchase.html',{'product':product})
    except:
        return redirect('index')


@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        user = request.user
        prod_id= request.POST['prod_id']
        quantity= int(request.POST['quant-t'])
        product = Product.objects.get(id=prod_id)
        email = user.email
        product.quantity -= quantity
        product.save()
        OrdItem = OrderedItem.objects.create(
            buyer_id=user.id,
            buyer_name= user.first_name,
            shop_id=product.store.id,
            shop_name=product.store.name,
            quantity=quantity,
            shipping_address=user.address,
            product_id=product.id,
            product_name=product.title,
            price=product.price
            )
        OrdItem.save()
        Total_Checkout = quantity*product.price
        send_mail(
        'New Order!',
        'You have one new order awaiting you in your EZMart shop!\nOrder ID: '
         + str(OrdItem.id) +
         '\nProduct:' + product.title + '\nAmount: '
        + str(quantity) + '\nTotal checkout: ' + str(Total_Checkout)
        + '$\nWill be shipped to Address: '
        + user.address +
        '\nPhone to contact with you:'+user.phone,
        'EZMartSCE@gmail.com',
        [email],
        fail_silently=False,)
    
        return redirect('index')
    else:
        return redirect('purchase')
