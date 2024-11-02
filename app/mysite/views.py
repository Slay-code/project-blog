from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Game, CategoryGame

def index(request):
    game = Game.objects.all().select_related('category', 'avtor').values(
        'id',
        'name',
        'slug',
        'description',
        'category__name',
        'avtor__username',
        'time_created',
    )
    context = {
        'title': 'Главная страница',
        'games': game,
    }
    
    return render(request, 'mysite/index.html', context)


def category(request, category_slug):
    category = get_object_or_404(CategoryGame, slug=category_slug)
    post = Game.objects.filter(category_id=category.pk).select_related('category').values(
        'id',
        'name',
        'slug',
        'description',
        'category__name',
        'avtor__username',
        'time_created',
    )
    
    context = {
        'title': f"категория - {category}",
        'posts': post,
    }
    
    return render(request, 'mysite/category.html', context)


def game_details(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    
    return render(request, 'mysite/game_details.html', {'title': game.name, 'game': game})



