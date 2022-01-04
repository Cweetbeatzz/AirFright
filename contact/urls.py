from django.urls.conf import path
from .views import contact_view

app_mmame = "contact"

urlpatterns = [
    path("contact", contact_view, name="contact"),
]
