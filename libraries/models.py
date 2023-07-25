import uuid
from django.db import models
from django.urls import reverse



class Library(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"Library - {self.label}"
    
    def get_absolute_url(self):
        return reverse("library_detail", args=[str(self.id)])