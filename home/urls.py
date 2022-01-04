from django.urls.conf import path
from .views import home_view

app_mmame = "home"

urlpatterns = [
    path("", home_view, name="home"),
]
