from django.urls.conf import path
from .views import about_view

app_mmame = "about"

urlpatterns = [
    path("about", about_view, name="about"),
]
