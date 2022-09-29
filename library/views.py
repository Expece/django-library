from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import BookForm
from .models import Book
from .utils import DataMixin

class Library(DataMixin, ListView):
    model = Book
    template_name = 'library/library.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().order_by('-published_date')

class AddBook(CreateView):
    form_class = BookForm
    template_name = 'library/addbook.html'
    success_url = reverse_lazy('library')

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

def _existBook(form: BookForm):
    books_from_db = Book.objects.all()
    new_book_author = form.cleaned_data['author']
    new_book_title = form.cleaned_data['title']
    for book in books_from_db:
        book_author, book_title = book.get_author_and_title()
        if book_author == new_book_author and book_title == new_book_title:
            return True
    return False

class BookPage(DetailView):
    model = Book
    template_name = 'library/bookpage.html'
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

class BooksByCategory(DataMixin, ListView):
    model = Book
    template_name = 'library/library.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs['category_slug']).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.kwargs['category_slug']
        return context

class Search(ListView):
    model = Book
    template_name = 'library/library.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)).order_by('-published_date')
        return books