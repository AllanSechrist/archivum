from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView, BookCreateView


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("add_book/", BookCreateView.as_view(), name="add_book"),
    path("search/", SearchResultsListView.as_view(), name="search_results")
]