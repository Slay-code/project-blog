from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from .forms import AddPostForm
from mysite.models import Game


# @login_required(login_url="users:anon")
# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(data=request.POST)
#         if form.is_valid():
#             avtor = form.save(commit=False)
#             avtor.avtor = request.user
#             avtor.save()
            
#             return redirect('mysite:home')
#     else:
#         form = AddPostForm()
            
#     context = {
#         'title': "Добавить пост",
#         'form': form,
#     }
    
#     return render(request, 'posts/add_post.html', context)


class AddPostView(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
    extra_context = {'title': 'Создать пост'}
    login_url = reverse_lazy('users:anon')
    
    def form_valid(self, form):
        avtor = form.save(commit=False)
        avtor.avtor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('mysite:home')


def del_post(request, game_id):
    post = get_object_or_404(Game, id=game_id, avtor=request.user)
    post.delete()
    return redirect("mysite:home")


# class DeletePostView(LoginRequiredMixin, DeleteView):


# login_required(login_url='users:login')
# def my_posts(request):
    
#     context = {
#         'posts': Game.objects.filter(avtor=request.user).select_related('category', 'avtor'),
#         'title': "Мои публикаци",
#     }
    
#     return render(request, 'posts/my_posts.html', context)
    
    
class MyPostsView(LoginRequiredMixin, ListView):
    template_name = 'posts/my_posts.html'
    context_object_name = 'posts'
    extra_context = {'title': "Мои публикаци"}
    login_url = 'users:login'
    
    def get_queryset(self):
        return Game.objects.filter(avtor=self.request.user).select_related('category', 'avtor')


# <form action="https://www.google.com/search" method="get">
#         <label for="search">Поиск:</label>
#         <input type="text" id="search" name="q" placeholder="Введите запрос" required>
#         <button type="submit">Поиск</button>
#     </form>