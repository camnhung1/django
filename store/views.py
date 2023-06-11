from locale import currency
from unicodedata import category
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm







# Create your views here.
def home(request):
    product= Product.objects.all()
    product_new=Product.objects.order_by('-created_at').all()[:4]
    page = Paginator(product, 8)
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
    context={'page':page,'product_new':product_new}
    return render(request,'store/index.html',context)

def collections(request):
    category=Category.objects.filter(status=0)
    context={'category': category}
    return render(request, 'store/collections.html',context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products':products, 'category':category}
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,'No such category found')
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            context={'products':products}
        else:
            messages.error(request,'No such product found')
            return redirect('collections')
    else:
        messages.error(request,'No such category found')
        return redirect('collections')
    return render(request,'store/products/view.html',context)

def productlistAjax(request):
    products=Product.objects.filter(status=0).values_list('name',flat=True)
    productsList=list(products)
    return JsonResponse(productsList, safe=False)

def searchproduct(request):
    if request.method=='POST':
        searchedterm=request.POST.get('keysearch')
        if searchedterm=="":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__contains=searchedterm).first()
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get("HTTP_REFERER"))
    return redirect(request.META.get('HTTP_REFERER'))

def aboutUS(request):
    return render(request,'store/about.html')

def myAccount(request):
    return render(request,'store/myaccount.html')

def contact(request):
    return render(request, 'store/contactus.html')

def lockout(request, credentials, *args, **kwargs):
    messages.error(request,'Your account has been locked because you failed to log in too many times')
    return render(request, 'store/auth/login.html')

@login_required(login_url="loginpage")
def userInfo(request):
    if request.method=='POST':
        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')
            userprofile.save()
    return render(request,'store/accountinfo.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'store/edit_profile.html', {'form': form})














