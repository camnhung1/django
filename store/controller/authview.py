from email import message
from re import X
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.models import *
from django.shortcuts import redirect, render
from store.forms import CustomUserForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from .token import account_activation_token

def activate(request, uidb64, token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,"Active successfully. Login to continute")
        return redirect('/login')
    else:
        messages.error(request,"Activation link Invalid")
    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject="Activate your user account"
    message = render_to_string("template_activate_account.html",{
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email=EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear { user }, please check email { to_email } inbox and click on \
            receive activation link to confirm and complete the register.') 
    else:
        messages.error(request, f'Problem sending email to { to_email }, check email address.')

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            email=form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
            else:
                user.is_active= False
                user.save()
                activateEmail(request,user, form.cleaned_data.get('email'))
                return redirect('home')
    context={'form':form}
    return render(request,'store/auth/register.html',context)

def loginpage(request):

    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            passwd=request.POST.get('password')
            user=authenticate(request,username=name,password=passwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged is Successfully')
                return redirect('/')
            else:
                messages.error(request,'Invalid Username or Password')
                return redirect('/login')
        return render(request, 'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
        return redirect('/')