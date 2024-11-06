from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('add-post/', views.AddPostView.as_view(), name='add_post'),
    path('delete-post/<int:game_id>/', views.del_post, name='del_post'),
    path('my-post/', views.MyPostsView.as_view(), name='my_posts'),
]
