from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView

from .models import Game, CategoryGame

# def index(request):
#     game = Game.objects.all().select_related('category', 'avtor')
    
#     context = {
#         'title': 'Главная страница',
#         'games': game,
#     }
    
#     return render(request, 'mysite/index.html', context)


class IndexView(ListView):
    queryset = Game.objects.all().select_related('category', 'avtor')
    template_name = "mysite/index.html"
    context_object_name = "games"
    extra_context = {'title': "Главная страница"}
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "Главная страница"
    #     context['games'] = self.queryset
    #     return context


# def category(request, category_slug):
#     category = get_object_or_404(CategoryGame, slug=category_slug)
#     post = Game.objects.filter(category_id=category.pk).select_related('category', 'avtor')
    
#     context = {
#         'title': f"категория - {category.name}",
#         'posts': post,
#     }
    
#     return render(request, 'mysite/category.html', context)


class GameCategoryView(ListView):
    template_name = "mysite/category.html"
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Game.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category', 'avtor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['posts'][0].category
        context["title"] = f"категория - {category}"
        return context


# def game_details(request, game_id, game_slug):
#     game = get_object_or_404(Game.objects.select_related('category', 'avtor'), id=game_id, slug=game_slug)
    
#     return render(request, 'mysite/game_details.html', {'title': game.name, 'game': game})


class GameDetailsView(DetailView):
    template_name = "mysite/game_details.html"
    pk_url_kwarg = 'game_id'
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'
    
    def get_object(self, queryset=None):
        game = Game.objects.select_related('category', 'avtor').get(id=self.kwargs[self.pk_url_kwarg], slug=self.kwargs[self.slug_url_kwarg])
        return game
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context