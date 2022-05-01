from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm


def library(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/library.html', {'books': books})


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
    return render(request, 'library/new_book.html', data)


def reader(request, author, title):
    book = get_object_or_404(Book, author=author, title=title)
    return render(request, 'library/reader.html', {'book': book})


def _check_repetition(form: BookForm):
    books_from_db = Book.objects.all()
    new_book_author = form.cleaned_data['author']
    new_book_title = form.cleaned_data['title']
    for book in books_from_db:
        book_author, book_title = book.get_author_and_title()
        if book_author == new_book_author and book_title == new_book_title:
            return 0
    return 1
