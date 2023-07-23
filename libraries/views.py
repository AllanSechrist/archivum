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

    