from django.shortcuts import render
from .models import Book

def library(request):
    books = Book.object.filter().order_by('-published_date')
    return render(request, 'library.html', {'books': books})
