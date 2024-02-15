from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="home"),
    path("test/", views.test_view, name="test_view"),
    path("browse/", views.browse, name="browse"),
    path("class/", views.SimpleClassBasedView.as_view(), name="class"),
]
