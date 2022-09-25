from atexit import register
from django import template
from library.models import Book, Category

register = template.Library()


@register.inclusion_tag('inc/_categorieslist.html')
def showCategories(selected_category_pk=None) -> list[Category]:
    categories = Category.objects.all()
    return {'categories': categories, 'selected_category_pk': selected_category_pk}
