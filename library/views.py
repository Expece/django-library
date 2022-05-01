from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm
from django.views.generic import UpdateView, DeleteView


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


def search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title=query)
    if not books:
        books = Book.objects.filter(author=query)
    return render(request, 'library/library.html', {'books': books})


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = '/library/'
    template_name = 'library/new_book.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/library/'
    template_name = 'library/delete_book.html'
    
    def get(self, request, pk):
        books = self.model.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, self.template_name, {'books': books})


def _check_repetition(form: BookForm):
    books_from_db = Book.objects.all()
    new_book_author = form.cleaned_data['author']
    new_book_title = form.cleaned_data['title']
    for book in books_from_db:
        book_author, book_title = book.get_author_and_title()
        if book_author == new_book_author and book_title == new_book_title:
            return False
    return True
