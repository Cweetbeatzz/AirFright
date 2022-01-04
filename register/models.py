from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    firstname = models.CharField( max_length=150)
    lastname = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField( max_length=150)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    confirmpassword = models.CharField(max_length=150)
    created_date = models.DateField()
     
    
