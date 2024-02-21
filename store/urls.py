from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="home"),
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("genres/", views.GenreListView.as_view(), name="genre_list"),
    path("contact/", views.contact, name="contact"),
]

