from ast import Or
from unicodedata import category, name
from urllib import request
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from store.models import Cart, Category, Order, OrderItem, Product, Profile
from django.contrib.auth.models import User
from django.db.models.functions import ExtractMonth
from django.db.models import Max, Min, Count, Avg, Sum 
from django.contrib import admin
import calendar

@login_required(login_url='loginpage')
def AnalyticsOrder(request):
    orders=Order.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(count=Count('id')).values('month','count')
    monthNumber=[]  
    totalOrders=[]
    for d in orders:
        monthNumber.append(calendar.month_name[d['month']])
        totalOrders.append(d['count'])
    return render(request,'store/analytics/orderbymonth.html',{'monthNumber':monthNumber,'totalOrders':totalOrders,'orders':orders})

@login_required(login_url='loginpage')
def AnalyticsSumPrice(request):
    sumorders=Order.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(sum=Sum('total_price')).values('month','sum')
    monthNum=[]  
    totalPrice=[]
    for t in sumorders:
        monthNum.append(calendar.month_name[t['month']])
        totalPrice.append(t['sum'])
    return render(request,'store/analytics/totalprice.html',{'monthNum':monthNum,'totalPrice':totalPrice,'sumorders':sumorders})

@login_required(login_url='loginpage')
def AnalyticsCountPro(request):
    category=Category.objects.all()
    productcount=Product.objects.values('category').annotate(count=Count('category')).order_by().values('category','count')
    cate=[]
    procount=[]
    
    for c in productcount:
        cate.append(c['category'])
        procount.append(c['count'])
    return render(request,'store/analytics/countpro.html',{'cate':cate,'procount':procount,'category':category,'productcount':productcount})