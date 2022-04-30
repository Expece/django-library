from xmlrpc.client import Boolean
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'main/home.html', {})


def library(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/library.html', {'books': books})


def about(request):
    return render(request, 'main/about.html', {})


def reader(request, author, title):
    book = get_object_or_404(Book, author=author, title=title)
    return render(request, 'main/reader.html', {'book': book})


def new_book(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid() and _check_repetition(form):
            form.save()
            return redirect('library')
        else:
            error = 'Form error'

    form = BookForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/new_book.html', data)


def _check_repetition(form: BookForm) -> Boolean:
    books_from_db = Book.objects.all()
    new_book_author = form.cleaned_data['author']
    new_book_title = form.cleaned_data['title']
    for book in books_from_db:
        book_author, book_title = book.get_author_and_title()
        if book_author == new_book_author and book_title == new_book_title:
            return 0
    return 1
