from users.models import User
from .models import Game


def q_search(query):
    if query.startswith('@'):
        return Game.objects.select_related('category', 'avtor').filter(avtor__username=query[1:])
