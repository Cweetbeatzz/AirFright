# from django.db import models
# from django.db.models.enums import Choices
# from django.db.models.fields import DateField, DateTimeField, IntegerField, TimeField
# from django.urls.base import reverse
# from django_countries.fields import CountryField

# # Create your models here.
# ############################################################################################
# class Airline(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     number = models.IntegerField(db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)

#     class Meta:
#         verbose_name_plural = "Flights"

#     def __str__(self):
#         return self.name


# ############################################################################################


# class City(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     # country = models.ForeignKey(
#     #     Country, related_name="country", null=False, on_delete=models.CASCADE
#     # )

#     class Meta:
#         verbose_name_plural = "Cities"

#     def __str__(self):
#         return self.name


# ############################################################################################


# class Country(models.Model):
#     name = CountryField()
#     slug = models.SlugField(max_length=100, unique=True)
#     city = models.ForeignKey(
#         City, related_name="city", null=False, on_delete=models.CASCADE
#     )

#     class Meta:
#         verbose_name_plural = "Countries"

#     def __str__(self):
#         return self.name


# ############################################################################################


# class Airports(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     country = models.ForeignKey(
#         Country, related_name="country", null=False, on_delete=models.CASCADE
#     )
#     city = models.ForeignKey(
#         City, related_name="city", null=False, on_delete=models.CASCADE
#     )

#     class Meta:
#         verbose_name_plural = "Airports"

#     def __str__(self):
#         return self.name


# ############################################################################################
# class Flight(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     flight_name = models.ForeignKey(Airline, null=False, on_delete=models.CASCADE)
#     flight_number = models.IntegerField()
#     airport_name = models.ForeignKey(
#         Airports, related_name="airport", null=False, on_delete=models.CASCADE
#     )
#     Depature_date = DateTimeField(auto_now_add=True)
#     Depature_day = DateField(auto_now_add=True)
#     Arrival_day = DateField(auto_now_add=True)
#     Arrival_date = DateTimeField(auto_now_add=True)
#     Depature_time = TimeField(auto_now=True)
#     Arrival_time = TimeField(auto_now=True)
#     Seat_number = IntegerField()
#     # flight_type = Choices()
#     country = models.ForeignKey(
#         Country, related_name="country", null=False, on_delete=models.CASCADE
#     )
#     city = models.ForeignKey(
#         City, related_name="city", null=False, on_delete=models.CASCADE
#     )

#     class Meta:
#         verbose_name_plural = "Flights"

#     def __str__(self):
#         return self.name
