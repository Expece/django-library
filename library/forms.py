from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title', 'text', 'category', 'cover')

        widgets = {
            "author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author',
            }),
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            }),
            "category": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category',
            }),
            "cover": forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }