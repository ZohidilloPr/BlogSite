from django.urls import path
from .views import HomeListView, Article_function


app_name = 'Blog'


urlpatterns = [
    path('', HomeListView.as_view(), name='Home'),
    path('post/<id>/', Article_function, name='Article'),
]
