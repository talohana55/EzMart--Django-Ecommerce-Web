from django.shortcuts import render
from .models import OrderedItem
from accounts.models import Account
import datetime
from django.utils import timezone
from django.utils.timezone import now

def receipts(request):
    sum = 0
    user = request.user   
    try:
        deltatime = 365
        if request.method == 'GET':
            deltatime = int(request.GET['delta']) if 'delta' in request.GET else 365
        delta = now() - timezone.timedelta(days=deltatime)
        orders = OrderedItem.objects.filter(buyer_id=user.id).filter(create_date__range=[delta, now()]).order_by('status')
        showDelta = 'Last Year'
        if deltatime == 90:
            showDelta = 'Last Three Months'
        elif deltatime == 30:
            showDelta = 'Last Month'
        elif deltatime == 7:
            showDelta = 'Last Week'
        elif  deltatime == 1:
            showDelta = 'Last Day'
        for order in orders:
                sum+= order.price * order.quantity
        context = {'orders': orders, 'sum':sum ,'ShowDelta':showDelta}
        return render(request, "receipts.html", context)
    except:
        return render(request, "receipts.html")
