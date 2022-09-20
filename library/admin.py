from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'cover', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('author', 'title')
    list_editable = ('published_date',)
    list_filter = ('published_date', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)