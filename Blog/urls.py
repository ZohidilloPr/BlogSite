from django.urls import path
from .views import (
    HomeListView,
    Article_function,
    BlogsCreateView,
    OneUserPostsListView,
    UserPostsListView,
    BlogsUpdateView,
    BlogsDeleteView,
    SearchResultsView,
)


app_name = 'Blog'


urlpatterns = [
    path('', HomeListView.as_view(), name='Home'),
    path('add', BlogsCreateView.as_view(), name='Add'),
    path('update/<pk>/', BlogsUpdateView.as_view(), name='Update'),
    path('delete/<pk>/', BlogsDeleteView.as_view(), name='Delete'),
    path('userposts', OneUserPostsListView.as_view(), name='UserPosts'),
    path('results/', SearchResultsView.as_view(), name='Search'),
    path('posts=<username>', UserPostsListView.as_view(), name='Posts'),
    path('post/<id>/', Article_function, name='Article'),
]
