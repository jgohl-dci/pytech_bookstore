from django.db import models


GENRE_CHOICES = (
        ("0", "None")
        ("1", "Romance"),
        ("2", "Sci-Fi"),
        ("3", "Fantasy"),
        ("4", "Drama"),
        ("5", "Poetry"),
        ("6", "Horror"),
    )


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default="0")
    date_of_birth = models.DateField(null=False)
    created_on = models.DateField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    num_of_books = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    author = models.CharField(max_length=200, null=False)
    summary = models.TextField(max_length=1000, null=False)
    isbn = models.CharField(max_length=13, unique=True, help_text="13 char string - ISBN Number")
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default="0")
    date_of_publishing = models.DateField()
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)  # 999.99
