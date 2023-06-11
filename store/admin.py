from dataclasses import fields
from json import load
from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from . models import Comment


class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product','product_qty','created_at']
    list_filter = ['created_at','user']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','Avartar','created_at']
    list_filter = ['created_at','name']
    readonly_fields =['Avartar']
    def Avartar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' width='50px'/>".format(img_url=lesson.image.name))
class ProductForm(forms.ModelForm):
    description=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductAdmin(admin.ModelAdmin):
    form=ProductForm
    list_display = ['name','Picture','category','selling_price','quantity']
    list_filter = ['category','created_at']
    readonly_fields = ['Picture']
    def Picture(self, pic):
        return mark_safe("<img src='/static/{img_url}' width='60px'/>".format(img_url=pic.product_image1.name))
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','fname','lname','address','state','city','country','phone','total_price','status']
    list_editable = ['status']
    list_filter = ['status']
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','price','quantity']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','state','city','country','pincode']
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Profile,ProfileAdmin)


admin.site.register(Comment)









