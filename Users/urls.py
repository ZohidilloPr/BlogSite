from django.urls import path
from .views import Home

app_name = 'Users'

urlpatterns = [
    path('', Home, name='Home')
]
