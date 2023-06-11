from dataclasses import field
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User, Comment
from django import forms






class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'id':'pw1','class':'form-control my-2','placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'id':'repw','class':'form-control my-2','placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']


class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter firt name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter last name'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter firt name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter last name'}))
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')















