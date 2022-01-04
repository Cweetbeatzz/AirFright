from django.shortcuts import render
from . import models

#######################################################################

# Create your views here.
def register_view(request):
    return render(request, "register.html")


#######################################################################


#######################################################################
