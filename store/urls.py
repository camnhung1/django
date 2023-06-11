from .import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy
from store.controller import authview, cart, wishlist,checkout,order,analytics






urlpatterns=[

    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    path('product-list',views.productlistAjax),
    path('searchproduct',views.searchproduct, name="searchproduct"),

    path('register/', authview.register, name='register'),
    path('login_account/', authview.loginpage, name='loginpage'),
    path('logout_account/', authview.logoutpage, name='logoutpage'),

    path('add-to-cart',cart.addtocart, name='addtocart'),
    path('cart',cart.viewcart, name="cart"),
    path('update-cart',cart.updatecart, name='updatecart'),
    path('delete-cart-item',cart.deletecartitem, name='deletecartitem'),
    
    path('wishlist',wishlist.viewwishlist,name="wishlist"),
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name="deletewishlistitem"),

    path('checkout',checkout.viewcheckout,name="checkout"),
    path('place-order',checkout.placeorder,name="placeorder"),
    path('proceed-to-pay',checkout.razorpaycheck),

    path('my-orders',order.vieworder, name="myorders"),
    path('details-orders/<str:t_no>',order.ordersdetails, name="ordersdetails"),

    path('analytics-orderbymonth',analytics.AnalyticsOrder, name="analyticsorderbymonth"),
    path('analytics-totalprice',analytics.AnalyticsSumPrice, name="analyticstotalprice"),
    path('analytics-countpro',analytics.AnalyticsCountPro, name="analyticscountpro"),

    path('about',views.aboutUS,name='about'),
    path('my-account',views.myAccount,name='myaccount'),
    path('contact-us',views.contact,name='contactus'),

    path('activate/<uidb64>/<token>',authview.activate, name="activate"),
    path('user-info',views.userInfo, name='userinfo'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="store/auth/password_reset.html"),
        name="reset_password"),
    path('reset_password_sent/',
        auth_views.PasswordChangeDoneView.as_view(template_name="store/auth/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="store/auth/password_reset_done.html"), 
        name="password_reset_complete"),
    path('edit/', views.edit_profile, name='edit'),

]