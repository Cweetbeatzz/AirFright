from django.forms.forms import Form
from django.shortcuts import render
from form import RegisterForm,formReg
from . import models
#######################################################################    

# Create your views here.
def register_view(request):
 return render(request,"register.html")
#######################################################################    
    
   

#######################################################################    
