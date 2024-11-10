from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('logout/', views.logout, name='logout'),
    path('anon/', views.ForAnonymUser.as_view(), name='anon'),
    path('profile-other-user/<slug:other_user>/', views.ProfileOtherUser.as_view(), name='other_user'),
]
