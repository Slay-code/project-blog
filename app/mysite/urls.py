from django.urls import path

from . import views


app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('game/<slug:game_slug>/', views.game_details, name='game_details'),
]
