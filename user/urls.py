from django.urls import path
from . import views


app_name = "user"

urlpatterns = [
    path("register/", views.user_registration, name="register"),
    path("login/", views.Login.as_view(), name="login"),
]
