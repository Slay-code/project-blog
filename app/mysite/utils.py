from users.models import User
from .models import Game


def q_search(query):
    if query.startswith('@'):
        return Game.objects.filter(avtor__username=query[1:])
