from django.contrib import admin
from store.models import Author, Book, Genre, StoreLocation, StoreManager


# Register your models here.
# admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(StoreLocation)
admin.site.register(StoreManager)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth',)
