from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("genre/", views.GenreListView.as_view(), name="genre_list"),
    # path("test/", views_example.test_view, name="test_view"),
    # path("browse/", views_example.browse, name="browse"),
    # path("class/", views_example.SimpleClassBasedView.as_view(), name="class"),
]
