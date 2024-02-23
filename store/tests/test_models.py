from django.test import TestCase
from store.models import Author


class TestAuthorModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name="John",
            last_name="Brown",
            email="jbrown@gmail.com",
            date_of_birth="1954-05-12",
            num_of_books=7,
            )

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "Date of birth")

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_first_name_comma_last_name(self):
        author = Author.objects.get(id=1)
        expected_name = f"{author.first_name} {author.last_name}"
        self.assertEqual(str(author), expected_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/store/authors/1/')
