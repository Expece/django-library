from cProfile import label
from django.urls import reverse
from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Book(models.Model):
    author = models.CharField(max_length=50, null=False, verbose_name='Author')
    title = models.CharField(max_length=50, null=False, verbose_name='Title')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    cover = models.ImageField(upload_to='covers/%Y/%m/%d',blank=True, null=True, verbose_name='Cover')
    published_date = models.DateTimeField(default=datetime.now(), verbose_name='Published date')

    def get_absolute_url(self):
        return reverse('readbook', kwargs = {'book_author': self.author, 'book_title': self.title})

    def __str__(self):
        return self.title

    def get_author_and_title(self):
        return self.author, self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']
    

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Category name')

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_title': self.title})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']