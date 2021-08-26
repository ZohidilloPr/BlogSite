from django.shortcuts import render, get_object_or_404
from .models import PostsModel
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
# Create your views here.


class HomeListView(ListView):
    model = PostsModel
    template_name = 'main/Home.html'
    ordering = '-pub_date'


class UserPostsListView(ListView):
    model = PostsModel
    template_name = 'main/userPosts.html'
    ordering = '-pub_date'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostsModel.objects.filter(author=user).order_by('-pub_date')


def Article_function(request, id):
    posts = PostsModel.objects.get(id=id)
    context = {
        'posts': posts,
        'id': id,
    }
    return render(request, 'main/Article.html', context)


class BlogsCreateView(CreateView):
    model = PostsModel
    template_name = 'main/Add_Post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class OneUserPostsListView(ListView):
    posts = PostsModel
    template_name = 'main/onlyOneUserPosts.html'
    ordering = '-pub_date'

    def get_queryset(self):
        return PostsModel.objects.filter(author=self.request.user).reverse()
