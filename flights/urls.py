from django.urls.conf import path

from flights.views import book_view, flights_details_view, flights_search_view

# app_name = "flights"

urlpatterns = [
    path("", book_view, name="book"),
    path("flight/details", flights_details_view, name="flightdetails"),
    path("flight/search", flights_search_view, name="flightsearch"),
]
