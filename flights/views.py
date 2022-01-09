from django.shortcuts import render

# Create your views here.


def book_view(request):
    return render(request, "book.html")


###########################################################################
def flights_search_view(request):
    return render(request, "book_flight_search.html")


###########################################################################


def flights_details_view(request):
    return render(request, "flight_details.html")


###########################################################################


def passenger_details_view(request):
    return render(request, "flight_details.html")


###########################################################################


def passenger_form_view(request):
    return render(request, "flight_details.html")


###########################################################################
