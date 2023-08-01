from django.urls import path

from .views import LibraryListView, LibraryDetailView, LibraryCreateView


urlpatterns = [
    path("", LibraryListView.as_view(), name="library_list"),
    path("add_library/", LibraryCreateView.as_view(), name="add_library"),
    path("<uuid:pk>", LibraryDetailView.as_view(), name="library_detail"),
]