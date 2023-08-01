from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from .models import Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = [
            "label",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            "",
            "label",
            ),
            Submit('submit', "Add Library", css_class="btn btn-primary")
        )