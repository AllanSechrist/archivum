from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.urls import reverse_lazy

from .models import BookMetaData, PhysicalBook
from .forms import BookForm, PhysicalBookForm


class BookListView(LoginRequiredMixin, ListView):
    """
    Allows the user to look at all the physical books
    that they have associated with there account.
    """
    model = PhysicalBook
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)



class BookDetailView(LoginRequiredMixin, DetailView): #PermissionRequiredMixin,
    """
    Displays information about an individual
    book.
    """
    model = PhysicalBook
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    # permission_required = "books.special_status" # TEST

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)
    

class BookCreateView(LoginRequiredMixin, CreateView):
    """
    A view that will add Meta Data about a book.
    Does not create a book that will be kept track of
    for purposes decided by the user.
    """
    model = BookMetaData
    form_class = BookForm
    template_name = 'books/add_book.html'
    login_url = "account_login"
    success_url = reverse_lazy("book_list")

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


class PhysicalBookCreateView(LoginRequiredMixin, CreateView):
    """
    Creates an object that is associated with the user
    and can be added to a library for organizational,
    inventory or any other purpose useful to the user.
    """
    model = PhysicalBook
    form_class = PhysicalBookForm
    template_name = "books/add_book_to_library.html"
    login_url = "account_login"
    success_url = reverse_lazy("book_list")

    def get_from_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SearchResultsListView(LoginRequiredMixin, ListView):
    """
    Allows a user to search for a book
    """
    model = PhysicalBook
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    login_url = "account_login"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return PhysicalBook.objects.filter(
            Q(title__icontains=query) & Q(user=self.request.user) | Q(author__icontains=query) & Q(user=self.request.user)
        )


