from typing import Any, Dict
from django.views.generic import ListView, DetailView

from .models import Library


class LibraryListView(ListView):
    model = Library
    context_object_name = "library_list"
    template_name = "libraries/library_list.html"


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    template_name = "libraries/library_detail.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.object
        books = library.book_set.all()
        context['books'] = books
        return context