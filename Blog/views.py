from django.shortcuts import render
from .models import PostsModel
from django.views.generic import ListView
# Create your views here.


class HomeListView(ListView):
    model = PostsModel
    template_name = 'main/Home.html'
    ordering = '-pub_date'


def Article_function(request, id):
    posts = PostsModel.objects.get(id=id)
    context = {
        'posts': posts,
        'id': id,
    }
    return render(request, 'main/Article.html', context)
