from django.urls import path
from .views import Home, SignUp_function, SignIn_function, SignOut_function

app_name = 'Users'

urlpatterns = [
    path('', Home, name='Home'),
    path('signup', SignUp_function, name='SignUp'),
    path('signin', SignIn_function, name='SignIn'),
    path('signout', SignOut_function, name='SignOut'),
]
