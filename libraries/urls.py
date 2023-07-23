from django.urls import path

from .views import LibraryListView, LibraryDetailView


urlpatterns = [
    path("", LibraryListView.as_view(), name="library_list"),
    path("<uuid:pk>", LibraryDetailView.as_view(), name="library_detail"),
]