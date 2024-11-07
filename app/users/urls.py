from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('anon/', views.ForAnonymUser.as_view(), name='anon'),
    path('profile-other-user/<str:other_user>/', views.profile_other_user, name='other_user'),
]
