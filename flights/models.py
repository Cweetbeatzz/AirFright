from django.db import models
from django.urls.base import reverse

# Create your models here.
############################################################################################
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Flights"

    def __str__(self):
        return self.name
