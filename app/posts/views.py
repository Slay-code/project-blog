from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import AddPostForm
from mysite.models import CategoryGame, Game


@login_required(login_url="users:anon")
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(data=request.POST)
        if form.is_valid():
            avtor = form.save(commit=False)
            avtor.avtor = request.user
            avtor.save()
            
            return redirect('mysite:home')
    else:
        form = AddPostForm()
            
    context = {
        'title': "Добавить пост",
        'form': form,
    }
    
    return render(request, 'posts/add_post.html', context)


@require_POST
def del_post(request, game_id):
    post = Game.objects.get(id=game_id, avtor=request.user)
    post.delete()
    return redirect("mysite:home")


login_required(login_url='users:login')
def my_posts(request):
    
    context = {
        'posts': Game.objects.filter(avtor=request.user).select_related('category', 'avtor'),
        'title': "Мои публикаци",
    }
    
    return render(request, 'posts/my_posts.html', context)
    