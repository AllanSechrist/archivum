from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from .models import Book
from libraries.models import Library


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publisher",
            "isbn",
            "level",
            "library",
        ]

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["library"].queryset = self.fields["library"].queryset.filter(user=user)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            "",
            "title",
            "author",
            "publisher",
            "isbn",
            "level",
            "library",
            ),
            Submit('submit', 'Add Book', css_class="btn btn-primary")
        )
