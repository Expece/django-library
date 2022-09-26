from django import forms
from .models import Book
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = Book
        fields = ['author', 'title', 'category', 'cover' ]

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pushkin A.S.'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'I remember a wonderful moment…'
            })
        }
