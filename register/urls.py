from .templates import create_view,delete_view,update_view
from django.urls import path


urlpatterns = [
    path('', create_view, name='register'),
    path('register', delete_view, name='register-delete'),
    path('login', update_view, name='register-update'),
]