from django.urls.conf import path

from flights.views import book_view

app_name = "flights"

urlpatterns = [
    path("", book_view, name="book"),
]
