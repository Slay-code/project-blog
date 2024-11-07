from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from .models import User
from mysite.models import Game


def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                messages.success(request, f"{user.username} Вы успешно вошли в аккаунт!")
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mysite:home'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)
        
    context = {
        'title': "Профиль",
        'form': form
    }
    
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))


class ForAnonymUser(TemplateView):
    template_name = "users/for_anonym_user.html"
    
    
def profile_other_user(request, other_user):
    context = {
        'user': get_object_or_404(User.objects.values('username', 'email'), username=other_user),
        'posts': Game.objects.select_related('category', 'avtor').filter(avtor__username=other_user)
    }
    
    return render(request, "users/profile_other_user.html", context)