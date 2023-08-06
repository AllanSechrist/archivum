from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView, BookCreateView, PhysicalBookCreateView


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("add_book/", BookCreateView.as_view(), name="add_book"),
    path("add_book_to_library/", PhysicalBookCreateView.as_view(), name="add_book_to_library"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]