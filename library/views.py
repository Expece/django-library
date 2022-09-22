from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404

from library.forms import BookForm
from .models import Book, Category

def library(request):
    books = Book.objects.filter().order_by('-published_date')
    categories = Category.objects.filter().all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'library/library.html', context)

def addbook(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid(): #  and not existBook(form):
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
    categories = Category.objects.filter().all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'library/library.html', context)

# def existBook(form: BookForm):
#     existBook = Book.objects.filter(author=form.changed_data['author'], title=form.changed_data['title'])
#     if existBook:
#         return True
#     return False