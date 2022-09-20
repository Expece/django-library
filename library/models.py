from django.urls import reverse
from django.db import models
from datetime import datetime

class Book(models.Model):
    author = models.CharField(max_length=50, null=False, verbose_name='Author')
    title = models.CharField(max_length=50, null=False, verbose_name='Title')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name='Cover')
    published_date = models.DateTimeField(default=datetime.now(), verbose_name='Published date')

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Category name')

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']