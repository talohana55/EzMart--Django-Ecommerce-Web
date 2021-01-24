from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Store
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from accounts.models import Account
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


def StoreHomePage(request):
    product = request.POST['store']
    product = Product.objects.get(id=product)
    products = Product.objects.filter(        store=product.store).filter(quantity__gte=1)
    return render(request, 'StoreHomePage.html', {'store': product.store, 'products': products})


def get_prods(self):  # helper queryset func
    # make a QuerySet out of the products DB (Matching class Product) wherein the 'store' attribute is equal to this objects (self)
    return Product.objects.filter(store=self)
    # the filter used is 'filter' rather than get, as 'get' only supports a single entity be returned, whereas 'filter' returns an "array" (QuerySet)

######################### STORE API #################################


@login_required(login_url='login')
def add_prod(request):
    if request.method == 'POST':
        user = request.user.username
        user = Account.objects.get(username=user)
        name = request.POST.get('nameProd')
        price = float(request.POST.get('priceProd'))
        cat = request.POST.get('category')
        desc = request.POST.get('desc')
        quan = int(request.POST.get('quantityProd'))
        pic = request.FILES['myfile'] if 'myfile' in request.FILES else False
        newP = Product(
            title=name,
            price=price,
            quantity=quan,
            category=cat,
            description=desc,
        )
        if(pic != False):
            fs = FileSystemStorage("static/images")
            fs.save(pic.name, pic)
            fileurl = "static/images" + fs.url(pic)
            newP.img = fileurl
        newP.store = user.store
        newP.save()
        return redirect('inventory')
    else:
        return render(request, 'inventory.html')


def delete_prod(request):
    try:
        if request.method == 'POST':
            id = int(request.POST.get('btn-prod-delete-click'))
            get_prods(request.user.store).get(id=id).delete()
            return redirect('inventory')
        else:
            return redirect('inventory')
    except ObjectDoesNotExist:
        return redirect('inventory')


def update_prod(request):  # update title / price / quantity

    try:
        if request.method == 'POST':
            id = int(request.POST.get('btn-prod-update-click'))
            Product.objects.filter(id=id)
            title = request.POST.get('prod-name')
            price = request.POST.get('prod-price')
            cat = request.POST.get('category')
            desc = request.POST.get('desc')
            quan = request.POST.get('quan-prod')
            pic = request.FILES['myfile'] if 'myfile' in request.FILES else False
            if(pic != False):
                fs = FileSystemStorage("static/images")
                fs.save(pic.name, pic)
                pic_url = "static/images" + fs.url(pic)
                Product.objects.filter(id=id).update(img=pic_url)
            if title != "":
                Product.objects.filter(id=id).update(title=title)
            if price != "":
                Product.objects.filter(id=id).update(price=float(price))
            if desc != "":
                Product.objects.filter(id=id).update(description=desc)
            if quan != "":
                Product.objects.filter(id=id).update(quantity=int(quan))
            if cat is not None:
                Product.objects.filter(id=id).update(category=cat)
            return redirect('inventory')
        else:
            return redirect('inventory')
    except ObjectDoesNotExist:
        print("oops, object doesn't exist!")
        return redirect('inventory')


@login_required(login_url='login')
def inventory(request):
    user = request.user.username
    user = Account.objects.get(username=user)
    if user.acc_type != 'B':
        return redirect('/')
    allProducts = get_prods(request.user.store)
    context = {'allProducts': allProducts}

    return render(request, 'inventory.html', context)


def shopView(request):
    stores = Store.objects.filter(status='C')
    context = {'stores': stores}
    return render(request, 'Stores.html', context)


def GoToStore(request):
    id = int(request.POST['store'])
    store = Store.objects.get(id=id)
    products = Product.objects.filter(store=store).filter(quantity__gte=1)
    return render(request, 'StoreHomePage.html', {'store': store, 'products': products})
