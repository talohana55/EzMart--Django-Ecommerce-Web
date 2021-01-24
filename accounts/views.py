from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Account
from Shop.models import Store
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from orders.models import OrderedItem
import datetime
from django.utils import timezone
from django.utils.timezone import now
import json


def registercustomer(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(first_name) < 2:
            messages.info(request, 'First name to short')
            return redirect('registercustomer')
        if len(last_name) < 2:
            messages.info(request, 'First name to short')
            return redirect('registercustomer')
        if len(username) < 6:
            messages.info(
                request, 'Username to short, should be atleast 6 symbols')
            return redirect('registercustomer')
        if len(address) < 6:
            messages.info(request, 'Address to short')
            return redirect('registercustomer')
        if len(phone) < 8:
            messages.info(request, 'Phone number to short')
            return redirect('registercustomer')
        if len(password1) < 6:
            messages.info(
                request, 'Password to short, should be atleast 6 symbols')
            return redirect('registercustomer')
        if password1 == password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('registercustomer')
            elif Account.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('registercustomer')
            else:
                user = Account.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    phone=phone,
                    password=password1
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registercustomer')

    else:
        return render(request, 'registercustomer.html')

    return render(request, 'registercustomer.html')


def Login(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'Login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def registerbusiness(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        businessnum = request.POST['businessnum']

        if len(businessnum) < 6:
            messages.info(request, 'Business number to short')
            return redirect('registerbusiness')
        if len(first_name) < 2:
            messages.info(request, 'First name to short')
            return redirect('registerbusiness')
        if len(last_name) < 2:
            messages.info(request, 'First name to short')
            return redirect('registerbusiness')
        if len(username) < 6:
            messages.info(
                request, 'Username to short, should be atleast 6 symbols')
            return redirect('registerbusiness')
        if len(address) < 6:
            messages.info(request, 'Address to short')
            return redirect('registerbusiness')
        if len(phone) < 8:
            messages.info(request, 'Phone number to short')
            return redirect('registerbusiness')
        if len(password1) < 6:
            messages.info(
                request, 'Password to short, should be atleast 6 symbols')
            return redirect('registerbusiness')
        if password1 == password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('registerbusiness')
            elif Account.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('registerbusiness')
            else:
                store1 = Store(
                    businessNum=int(businessnum)
                )
                user = Account.objects.create_business_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    phone=phone,
                    username=username,
                    password=password1,
                )
                store1.save()
                user.store = store1
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registerbusiness')

    else:
        return render(request, 'registerbusiness.html')

    return render(request, 'registerbusiness.html')


@login_required(login_url='login')
def userProfile(request):
    user = request.user.username
    u = Account.objects.get(username=user)
    if u.acc_type == 'B':
        return redirect('businessProfile')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        cur_password = request.POST['cur_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if u is not None and u.check_password(cur_password):
            if password1 == password2:
                if Account.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('userProfile')
                else:
                    flag = False
                if first_name != '':
                    u.first_name = first_name
                    flag = True
                if last_name != '':
                    u.last_name = last_name
                    flag = True
                if phone != '':
                    u.phone = phone
                    if len(phone) < 8:
                        messages.info(request, 'Phone number to short')
                        return redirect('userProfile')
                    else:
                        u.phone = phone
                        flag = True
                if email != '':
                    u.email = email
                    flag = True
                if address != '':
                    u.address = address
                    flag = True
                if password1 != '':
                    if len(password1) < 6:
                        messages.info(
                            request, 'Password to short, should be atleast 6 symbols')
                        return redirect('userProfile')
                    else:
                        flag = True
                        u.set_password(password1)
                if flag:
                    u.save()
                return redirect('userProfile')

            else:
                messages.info(request, 'Passwords do not match')
                return redirect('userProfile')
        else:
            messages.info(request, 'Current Password do not match')
            return redirect('userProfile')
    else:
        return render(request, 'userProfile.html')


@login_required(login_url='login')
def businessProfile(request):
    user = request.user.username
    u = Account.objects.get(username=user)
    if u.acc_type != 'B':
        return redirect('userProfile')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        cur_password = request.POST['cur_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if u is not None and u.check_password(cur_password):
            if password1 == password2:
                if Account.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('businessProfile')
                else:
                    flag = False
                if first_name != '':
                    u.first_name = first_name
                    flag = True
                if last_name != '':
                    u.last_name = last_name
                    flag = True
                if phone != '':
                    u.phone = phone
                    if len(phone) < 8:
                        messages.info(request, 'Phone number to short')
                        return redirect('businessProfile')
                    else:
                        u.phone = phone
                        flag = True
                if email != '':
                    u.email = email
                    flag = True
                if address != '':
                    u.address = address
                    flag = True
                if password1 != '':
                    if len(password1) < 6:
                        messages.info(
                            request, 'Password to short, should be atleast 6 symbols')

                        return redirect('businessProfile')
                    else:
                        flag = True
                        u.set_password(password1)
                if flag:
                    u.save()
                return redirect('businessProfile')

            else:
                messages.info(request, 'Passwords do not match')
                return redirect('businessProfile')
        else:
            messages.info(request, 'Current Password do not match')
            return redirect('businessProfile')
    else:
        return render(request, 'businessProfile.html')


@login_required(login_url='login')
def Business(request):
    user = request.user.username
    u = Account.objects.get(username=user)
    if request.method == 'POST':
        store_name = request.POST['businessName']
        address = request.POST['address']
        phone = request.POST['phone']
        category = request.POST['category']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        twitter = request.POST['twitter']
        pic = request.FILES['img_one'] if 'img_one' in request.FILES else False

        if u is not None:
            flag = False
            if(pic != False):
                fs = FileSystemStorage("static/images")
                fs.save(pic.name, pic)
                pic_url = "static/images" + fs.url(pic)
                store = u.store
                store.logo_img = pic_url
                store.save()
            if store_name != '':
                if 2 < len(store_name) < 15:
                    u.store.name = store_name
                    flag = True
            if category != '':
                u.store.category = category
                flag = True
            if facebook != '':
                u.store.facebook_url = facebook
                flag = True
            if instagram != '':
                u.store.instagram_url = instagram
                flag = True
            if twitter != '':
                u.store.twitter_url = twitter
                flag = True

            if phone != '':
                if len(phone) < 8:
                    messages.info(request, 'Phone number to short')
                    return redirect('Business')
                else:
                    u.store.phone = phone
                    flag = True
            if address != '':
                u.store.address = address
                flag = True
            if flag:
                u.store.save()
                u.save()
            return redirect('Business')
        else:
            return render(request, 'Business.html')
    else:
        return render(request, 'Business.html')


@login_required(login_url='login')
def ordersManage(request):
    if request.user.acc_type != 'B':
        redirect('index')
    user = request.user
    try:
        deltatime = 365
        if request.method == 'GET':
            deltatime = int(request.GET['delta']
                            ) if 'delta' in request.GET else 365
        delta = now() - timezone.timedelta(days=deltatime)
        orders = OrderedItem.objects.filter(shop_id=user.store.id).filter(
            create_date__range=[delta, now()]).order_by('status')
        showDelta = 'Last Year'
        if deltatime == 90:
            showDelta = 'Last Three Months'
        elif deltatime == 30:
            showDelta = 'Last Month'
        elif deltatime == 7:
            showDelta = 'Last Week'
        elif deltatime == 1:
            showDelta = 'Last Day'
        context = {'orders': orders, 'ShowDelta': showDelta}
        return render(request, "ordersManage.html", context)
    except:
        return render(request, "ordersManage.html")


@login_required(login_url='login')
def ship(request):
    if request.user.acc_type != 'B':
        redirect('index')
    if request.method == 'POST':
        id = int(request.POST['ship'])
        order = OrderedItem.objects.get(id=id)
        print(order)
        order.status = 'Shipped'
        order.save()
    return redirect('ordersManage')


class sold_prods():  # helping class for selling report func
    def __init__(self, id, name, price, income, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.income = income

    def __str__(self):
        return str(self.id)


def get_index(lst, value):  # help function for selling report func
    for index, item in enumerate(lst):
        if item.id == value:
            return index
    return -1


@login_required(login_url='login')
def sellingreport(request):
    if request.user.acc_type != 'B':
        redirect('index')
    user = request.user
    try:
        deltatime = 365
        if request.method == 'GET':
            deltatime = int(request.GET['delta']
                            ) if 'delta' in request.GET else 365
        delta = now() - timezone.timedelta(days=deltatime)
        orders = OrderedItem.objects.filter(shop_id=user.store.id).filter(
            create_date__range=[delta, now()]).order_by('status')
        showDelta = 'Last Year'
        if deltatime == 90:
            showDelta = 'Last Three Months'
        elif deltatime == 30:
            showDelta = 'Last Month'
        elif deltatime == 7:
            showDelta = 'Last Week'
        elif deltatime == 1:
            showDelta = 'Last Day'
        solds = []
        for order in orders:
            if any(sold.id == str(order.product_id) for sold in solds):
                index = get_index(solds, str(order.product_id))
                if index != -1:
                    solds[index].quantity += order.quantity
                    solds[index].income += order.price*order.quantity
            else:
                prod = sold_prods(str(order.product_id), order.product_name,
                                  order.price, order.quantity*order.price, order.quantity)
                solds.append(prod)
        total_income = 0
        for sold in solds:
            total_income += sold.income
        context = {'orders': solds, 'ShowDelta': showDelta,
                   'total_income': total_income}
        return render(request, "sellingreport.html", context)
    except:
        return render(request, "sellingreport.html")
