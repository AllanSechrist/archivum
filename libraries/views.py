from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Library


class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    context_object_name = "library_list"
    template_name = "libraries/library_list.html"


class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library
    context_object_name = "library"
    template_name = "libraries/library_detail.html"
