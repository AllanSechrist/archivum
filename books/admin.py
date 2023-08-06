from django.contrib import admin
from .models import BookMetaData, PhysicalBook


@admin.register(BookMetaData)
class BookMetaDataAdmin(admin.ModelAdmin):
    list_display = ("level", "title", "author", "publisher", "isbn")


@admin.register(PhysicalBook)
class PhysicalBookAdmin(admin.ModelAdmin):
    list_display = ("book", "library")