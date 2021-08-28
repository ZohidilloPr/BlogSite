from django.shortcuts import render, get_object_or_404
from .models import PostsModel
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

# Create your views here.


class HomeListView(ListView):
    model = PostsModel
    template_name = 'main/Home.html'
    ordering = '-pub_date'
    paginate_by = 3


class SearchResultsView(ListView):
    model = PostsModel
    template_name = 'main/search.html'
    ordering = '-pub_date'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PostsModel.objects.filter(Q(title__icontains=query))
        return object_list


class UserPostsListView(ListView):
    model = PostsModel
    template_name = 'main/userPosts.html'
    ordering = '-pub_date'
    paginate_by = 2

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


class BlogsUpdateView(UpdateView, UserPassesTestMixin):
    model = PostsModel
    template_name = 'main/Update.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_function(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogsDeleteView(DeleteView, UserPassesTestMixin):
    model = PostsModel
    template_name = 'main/Delete.html'
    success_url = '/'

    def test_function(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class OneUserPostsListView(ListView):
    posts = PostsModel
    template_name = 'main/onlyOneUserPosts.html'
    ordering = '-pub_date'
    paginate_by = 2

    def get_queryset(self):
        return PostsModel.objects.filter(author=self.request.user).reverse()
