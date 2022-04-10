from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # If User is deleted then delete books associated with that user
    book_title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.book_title


class BookNote(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE
    )  # If a Book is deleted then delete notes associated with that book
    note_chapter_title = models.CharField(max_length=255)
    note_chapter_text = models.TextField

    def __str__(self):
        return self.note_chapter_title
