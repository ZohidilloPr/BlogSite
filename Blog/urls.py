from django.urls import path
from .views import (
    HomeListView,
    Article_function,
    BlogsCreateView,
    OneUserPostsListView
)


app_name = 'Blog'


urlpatterns = [
    path('', HomeListView.as_view(), name='Home'),
    path('add', BlogsCreateView.as_view(), name='Add'),
    path('userposts', OneUserPostsListView.as_view(), name='UserPosts'),
    path('post/<id>/', Article_function, name='Article'),
]
