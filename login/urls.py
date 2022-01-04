from django.urls.conf import path
from .views import login_view

app_mmame = "login"

urlpatterns = [
    path("login", login_view, name="login"),
]
