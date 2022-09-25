from atexit import register
from django import template
from library.models import Book, Category

register = template.Library()


@register.inclusion_tag('inc/_categorieslist.html')
def showCategories() -> list[Category]:
    categories = Category.objects.all()
    return {'categories': categories}
