from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required

from store.models import Order,OrderItem

@login_required(login_url="loginpage")
def vieworder(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'store/orders/index.html',context)
@login_required(login_url="loginpage")
def ordersdetails(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems =OrderItem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request,'store/orders/ordersdetails.html',context)