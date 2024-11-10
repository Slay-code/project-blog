from django.views.generic import ListView, DetailView

from .models import Game
from .utils import q_search

# def index(request):
#     game = Game.objects.all().select_related('category', 'avtor')
    
#     context = {
#         'title': 'Главная страница',
#         'games': game,
#     }
    
#     return render(request, 'mysite/index.html', context)


class IndexView(ListView):
    template_name = "mysite/index.html"
    context_object_name = "games"
    extra_context = {'title': "Главная страница"}
    
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query:
            game = q_search(query)
        else:
            game = Game.objects.all().select_related('category', 'avtor')
            
        return game


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
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'
    
    def get_object(self, queryset=None):
        game = Game.objects.select_related('category', 'avtor').get(slug=self.kwargs[self.slug_url_kwarg])
        return game
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context
