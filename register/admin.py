from django.contrib import admin

# Register your models here.
from . import models
import register

admin.site.register(models.User)
