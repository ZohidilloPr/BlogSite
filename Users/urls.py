from django.urls import path
from .views import Home, SignUp_function

app_name = 'Users'

urlpatterns = [
    path('', Home, name='Home'),
    path('signup', SignUp_function, name='SignUp'),
]
