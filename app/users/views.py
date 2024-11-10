# from django.db.models.base import Model as Model
from django.shortcuts import redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.contrib.auth.views import LoginView

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from .models import User
from mysite.models import Game


# def login(request):
    
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 messages.success(request, f"{user.username} Вы успешно вошли в аккаунт!")
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('mysite:home'))
#     else:
#         form = UserLoginForm()
    
#     context = {
#         'title': 'Авторизация',
#         'form': form,
#     }
    
#     return render(request, 'users/login.html', context)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    extra_context = {'title': 'Авторизация'}
    
    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('users:logout'):
            return redirect_page
        return reverse_lazy("mysite:home")


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = UserRegistrationForm()
    
#     context = {
#         'title': 'Регистрация',
#         'form': form,
#     }
    
#     return render(request, 'users/register.html', context)


class UserRegistrationView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("mysite:home")
    extra_context = {'title': 'Регистрация'}
    
    def form_valid(self, form):
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user=user)
            
        return redirect(self.success_url)


# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile')
#     else:
#         form = ProfileForm(instance=request.user)
        
#     context = {
#         'title': "Профиль",
#         'form': form
#     }
    
#     return render(request, 'users/profile.html', context)


class UserProfileView(UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")
    extra_context = {'title': 'Профиль'}
    
    def get_object(self, queryset=None):
        return self.request.user


def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))


class ForAnonymUser(TemplateView):
    template_name = "users/for_anonym_user.html"
    
    
# def profile_other_user(request, other_user):
#     context = {
#         'user': get_object_or_404(User.objects.values('username', 'email'), username=other_user),
#         'posts': Game.objects.select_related('category', 'avtor').filter(avtor__username=other_user)
#     }
    
#     return render(request, "users/profile_other_user.html", context)


class ProfileOtherUser(ListView):
    template_name = "users/profile_other_user.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        return Game.objects.filter(avtor__username=self.kwargs["other_user"]).select_related('category', 'avtor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User.objects.values('username', 'email'), username=self.kwargs['other_user'])
        return context
    
    
    
    