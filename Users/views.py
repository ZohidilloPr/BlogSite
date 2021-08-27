from .forms import UserForm, UpdateUser, UpdateProfile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import UserProfile

# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)

    return render(request, 'index/UserHome.html')


def SignUp_function(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome New User')
            return redirect('Users:Home')
    form = UserForm
    return render(request, 'register/signUp.html', context={'form': form})


def SignIn_function(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Good Job {user.username}')
                return redirect('Users:Home')
            else:
                messages.error(request, 'Something went to wrong!')
        else:
            messages.error(request, 'Something went to wrong!')
    forms = AuthenticationForm
    return render(request, 'register/signIn.html', context={'login_form': forms})


def SignOut_function(request):
    logout(request)
    messages.info(request, 'Good Bie :( ')
    return redirect('Blog:Home')


def Settings_function(request):
    if request.method == 'POST':
        form_u = UpdateUser(data=request.POST, instance=request.user)
        form_p = UpdateProfile(request.POST, request.FILES,
                               instance=request.user.userprofile)
        if form_u.is_valid() and form_p.is_valid():
            form_u.save()
            form_p.save()
            messages.success(request, 'User UPDATED')
            return redirect('Users:Home')
    else:
        form_u = UpdateUser(instance=(request.user))
        form_p = UpdateProfile(instance=(request.user.userprofile))
    context = {
        'form_u': form_u,
        'form_p': form_p,
    }
    return render(request, 'register/Settings.html', context)
