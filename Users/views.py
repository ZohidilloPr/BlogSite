from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login
# from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, 'index/UserHome.html')


def SignUp_function(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Users:Home')
    form = UserForm
    return render(request, 'register/signUp.html', context={'form': form})
