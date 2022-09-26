from django.urls import reverse
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class Book(models.Model):
    author = models.CharField(max_length=50, null=False, verbose_name='Author')
    title = models.CharField(max_length=50, null=False, verbose_name='Title')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    cover = models.ImageField(upload_to='covers/%Y/%m/%d',blank=True, null=True, verbose_name='Cover')

    published_date = models.DateTimeField(default=datetime.now(), verbose_name='Published date')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('BookPage', kwargs = {'book_slug': self.slug})

    def __str__(self):
        return self.title

    def get_author_and_title(self):
        return self.author, self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify((self.author+' '+self.title))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']
    

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Category name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('BooksByCategory', kwargs = {'category_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']