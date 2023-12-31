import uuid
import string
from django.db import models
from django.urls import reverse
from django.conf import settings


def generate_level_choices():
    """
    Creates level choices for books.
    The levels a book can be are shown by the
    letters A ~ R
    """
    levels = list(string.ascii_uppercase)[:18] # creates letters A ~ R
    choices = [(level, level) for level in levels]
    return choices


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=15, null=True, blank=True) # if a book does not have an ISBN leave blank.
    level = models.CharField(max_length=1, null=True, blank=True, choices=generate_level_choices())
    library = models.ForeignKey("libraries.Library", on_delete=models.SET_NULL, null=True, related_name="books") # set to null when library is deleted.

    # class Meta: # TEST
    #     permissions = [
    #         ("special_status", "Can read all books"),
    #     ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])