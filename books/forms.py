from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from .models import BookMetaData, PhysicalBook
from libraries.models import Library


class BookForm(forms.ModelForm):
    class Meta:
        model = BookMetaData
        fields = [
            "title",
            "author",
            "publisher",
            "isbn",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            "",
            "title",
            "author",
            "publisher",
            "isbn",
            ),
            Submit('submit', 'Add Book', css_class="btn btn-primary")
        )
    library = forms.ModelChoiceField(queryset=Library.objects.all(), required=False)

    def save(self, commit=True):
        book_metadata = super().save(commit=False)

        if commit:
            book_metadata.save()

            library = self.cleaned_data.get('library')
            if library is not None:
                physical_book = PhysicalBook(book=book_metadata, library=library)
                physical_book.save()
            else:
                physical_book = PhysicalBook(book=book_metadata)
                physical_book.save()

        return book_metadata
    

class PhysicalBookForm(forms.ModelForm):
    class Meta:
        model = PhysicalBook
        fields = [
            "library",
            "level",
        ]

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["library"].queryset = self.fields["library"].queryset.filter(user=user)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            "",
            "library",
            "level",
            )
        )