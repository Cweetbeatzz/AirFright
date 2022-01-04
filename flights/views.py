from django.shortcuts import render

# Create your views here.


def book_view(request):
    return render(request, "book.html")


def flights_details_view(request):
    pass
