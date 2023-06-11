from store.models import Cart, Product, Profile
from django.db.models import Count
from django.contrib.auth.models import User


def quantityCart(request):
    qtycart=None
    quantity=[]
    sl=0
    if request.user.is_authenticated:
        qtycart=Cart.objects.annotate(count=Count('id')).values('count').filter(user=request.user)  
        for i in qtycart:
            quantity.append(i['count'])
        for qty in quantity:
            sl = sl + qty
    return {'sl':sl} 


def infoCart(request):
    cart=None
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
    return {'cart': cart} 

def dataCatePro(request):
    catepro=None
    if request.user.is_authenticated:
        catepro= Product.objects.order_by('created_at').all()
    return {'catepro':catepro}

   