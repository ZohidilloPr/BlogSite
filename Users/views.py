from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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


def SignIn_function(request):
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Users:Home')
            else:
                return messages.error(request, 'Something went to wrong!')
        else:
            return messages.error(request, 'Something went to wrong!')
    forms = AuthenticationForm
    return render(request, 'register/signIn.html', context={'login_form': forms})


def SignOut_function(request):
    logout(request)
    return redirect('Blog:Home')
