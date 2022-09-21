from django.shortcuts import render, redirect, get_object_or_404

from library.forms import BookForm
from .models import Book

def library(request):
    books = Book.objects.filter().order_by('-published_date')
    return render(request, 'library/library.html', {'books': books})

def addbook(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid() and not existBook(form):
            form.save()
            return redirect('library')
        else:
            error='Form error'
    form = BookForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'library/addbook.html', context)

def readbook(request, book_id):
    bookItem = get_object_or_404(Book, pk=book_id)
    context = {
        'bookItem': bookItem,
    }
    return render(request, 'library/readbook.html', context)


def existBook(form: BookForm):
    existBook = Book.objects.filter(author=form.changed_data['author'], title=form.changed_data['title'])
    if existBook:
        return True
    return False