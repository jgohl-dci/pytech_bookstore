from django.http import HttpResponse
from .models import Author, Book, Genre
from django.views import View
from django.urls import reverse


def index(request):
    authors_link = f"<a href={reverse('store:author_list')}>Authors</a>"
    books_link = f"<a href={reverse('store:book_list')}>Books</a>"
    genres_link = f"<a href={reverse('store:genre_list')}>Genres</a>"

    content = f"<h3>Bookstore</h3><ul><li>{authors_link}</li> <li>{books_link}</li> <li>{genres_link}</li></ul>"

    return HttpResponse(content)


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        content = "<h3>Authors:</h3>"

        for author in authors:
            new_author = f"<li>{author.first_name} {author.last_name}</li>"
            content += new_author

        return HttpResponse(content)


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        content = "<h3>Books:</h3>"

        for book in books:
            new_book = f"<li>{book.title} - written by: {book.author}</li>"
            content += new_book

        return HttpResponse(content)


class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()
        content = "<h3>Genres:</h3>"

        for genre in genres:
            new_genre = f"<li>{genre}</li>"
            content += new_genre

        return HttpResponse(content)
