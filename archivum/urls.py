from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("books/", include("books.urls")),
    path("libraries/", include("libraries.urls")),
    path("", include("pages.urls")),
]
