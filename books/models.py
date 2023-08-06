from typing import Set
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



class BookMetaData(models.Model):
    """
    Creates meta data for a book. To be linked to physical books.
    In the case that a book doesn't have an ISBN number,
    The user can create a unique "ISBN".
    It is recommened to use letters, a combinations of
    letters and numbers, or create an "ISBN" that
    is less than 10 characters in length inorder to prevent accidently
    assigning an ISBN that might exsist. 
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=15, unique=True) 

    # class Meta: # TEST
    #     permissions = [
    #         ("special_status", "Can read all books"),
    #     ]

    def __str__(self):
        return self.title



class PhysicalBook(models.Model):
    LEVEL_CHOICES = generate_level_choices()
    library = models.ForeignKey("libraries.Library", on_delete=models.SET_NULL, null=True, blank=True, related_name="books") # set to null when library is deleted.
    book = models.ForeignKey(BookMetaData, on_delete=models.CASCADE, related_name="book")
    level = models.CharField(max_length=1, null=True, blank=True, choices=LEVEL_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="books", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    