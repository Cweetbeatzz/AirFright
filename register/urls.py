from django.urls import path

from register.views import register_view

app_name = "register"
urlpatterns = [
    path("register", register_view, name="register"),
]
