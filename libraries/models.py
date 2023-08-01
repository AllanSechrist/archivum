import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings



class Library(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    label = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="libraries", on_delete=models.CASCADE)

    def __str__(self):
        return f"Library - {self.label}"
    
    def get_absolute_url(self):
        return reverse("library_detail", args=[str(self.id)])