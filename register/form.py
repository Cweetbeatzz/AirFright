from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
 class Meta:
  model = User
  fields = [
    'firstname' ,
    'lastname' ,
    'username' ,
    'email' , 
    'address' ,
    'phone' , 
    'state' ,
    'country' ,
    'gender' ,
    'password' ,
    'confirmpassword' , 
   
  ]
  
class formReg(forms.Form):
    firstname = forms.CharField(required=True, max_length=150)
    lastname = forms.CharField(required=True,max_length=150)
    username = forms.CharField(required=True,max_length=150)
    email = forms.EmailField(required=True, max_length=150)
    address = forms.CharField(required=True,max_length=150)
    phone = forms.CharField(required=True,max_length=150)
    state = forms.CharField(required=True,max_length=150)
    country = forms.CharField(required=True,max_length=150)
    gender = forms.CharField(required=True,max_length=150)
    password = forms.CharField(required=True,max_length=150)
    confirmpassword = forms.CharField(required=True,max_length=150)