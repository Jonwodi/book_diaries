from django.contrib import admin

from .models import Book, BookNote


@admin.register(Book)
class Book(admin.ModelAdmin):
    pass


@admin.register(BookNote)
class BookNote(admin.ModelAdmin):
    pass
