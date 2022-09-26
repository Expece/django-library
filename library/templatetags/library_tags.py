from atexit import register
from django import template
from library.models import Category

register = template.Library()


@register.inclusion_tag('inc/_categorieslist.html')
def showCategories(selected_category=None) -> list[Category]:
    categories = Category.objects.all()
    return {'categories': categories, 'selected_category': selected_category}
