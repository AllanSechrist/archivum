from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

from .models import Library
from .forms import LibraryForm


class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    context_object_name = "library_list"
    template_name = "libraries/library_list.html"
    login_url = "account_login"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)

class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library
    context_object_name = "library"
    template_name = "libraries/library_detail.html"
    login_url = "account_login"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)
    

class LibraryCreateView(LoginRequiredMixin, CreateView):
    model = Library
    form_class = LibraryForm
    template_name = "libraries/add_library.html"
    login_url = "account_login"
    success_url = reverse_lazy("library_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
