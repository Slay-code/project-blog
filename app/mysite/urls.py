from django.urls import path

from . import views


app_name = 'mysite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('search/', views.IndexView.as_view(), name='search'),
    path('category/<slug:category_slug>/', views.GameCategoryView.as_view(), name='category'),
    path('game/<int:game_id>/<slug:game_slug>/', views.GameDetailsView.as_view(), name='game_details'),
]
