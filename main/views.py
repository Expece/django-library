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


def reader(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'main/reader.html', {'book': book})


def new_book(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')
        else:
            error = 'Form error'

    form = BookForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/new_book.html', data)
