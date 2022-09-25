from django.shortcuts import render, redirect, get_object_or_404

from library.forms import BookForm
from .models import Book, Category

def library(request):
    books = Book.objects.filter().order_by('-published_date')
    context = {
        'books': books,
    }
    return render(request, 'library/library.html', context)

def addbook(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid() and not _existBook(form):
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

def readbook(request, book_author, book_title):
    book = get_object_or_404(Book, author=book_author, title=book_title)  
    context = {
        'book': book,
    }
    return render(request, 'library/readbook.html', context)

def getBooksByCategory(request, category_title):
    category = Category.objects.get(title=category_title)
    books = Book.objects.filter(category=category.pk).all()
    context = {
        'books': books,
    }
    return render(request, 'library/library.html', context)

def search(request):
    query = request.GET.get('q')
    query = query[0].upper() + query[1:]
    books = Book.objects.filter(title=query)

    if not books:
        books = Book.objects.filter(author=query)
    context = {
        'books': books,
    }
    return render(request, 'library/library.html', context)

def _existBook(form: BookForm):
    books_from_db = Book.objects.all()
    new_book_author = form.cleaned_data['author']
    new_book_title = form.cleaned_data['title']
    for book in books_from_db:
        book_author, book_title = book.get_author_and_title()
        if book_author == new_book_author and book_title == new_book_title:
            return True
    return False