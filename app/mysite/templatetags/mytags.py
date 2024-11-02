from django import template
from django.utils.http import urlencode
from django.core.cache import cache

from mysite.models import CategoryGame, Game


register = template.Library()

# @register.simple_tag()
# def tag_categories():
#     return CategoryGame.objects.values('slug', 'name')


# Это от чата gpt
@register.simple_tag()
def tag_categories():
    categories = cache.get('category_game_list')
    
    if categories is None:
        categories = list(CategoryGame.objects.only('slug', 'name').all())
        cache.set('category_game_list', categories, timeout=3600)  # Кэш на 1 час
    
    return categories





