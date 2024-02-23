from django.test import TestCase
from store.models import Book, Author, Genre
from django.urls import reverse
# from store.views import


class TestBookListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name="John",
            last_name="Brown",
            email="jbrown@gmail.com",
            date_of_birth="1954-05-12",
            num_of_books=7,
            )

        Genre.objects.create(name="Programming")

        author = Author.objects.get(id=1)
        # genre = Genre.objects.get(id=1)

        Book.objects.create(
            title="Test title",
            author=author,
            summary="bla bla bla",
            isbn="1234567891234",
            # genre=genre,
            date_of_publishing="2014-06-02",
            in_stock=True,
            price=14.95,
        )

        Book.objects.create(
            title="Test title2",
            author=author,
            summary="bla bla bla",
            isbn="1234567891235",
            # genre=genre,
            date_of_publishing="2014-06-06",
            in_stock=True,
            price=99.95,
        )

        book = Book.objects.get(id=1)
        book.genre.set((1,))
        book2 = Book.objects.get(id=2)
        book2.genre.set((1,))

    def test_view_url_exists_desired_location(self):
        response = self.client.get('/store/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("store:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/book_list.html")

    def test_list_all_books(self):
        response = self.client.get(reverse("store:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 2)
