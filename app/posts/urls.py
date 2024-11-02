from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('add-post/', views.add_post, name='add_post'),
    path('delete-post/<int:game_id>/', views.del_post, name='del_post'),
]
