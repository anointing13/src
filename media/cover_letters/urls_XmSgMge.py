from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *
from .views import profile


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', Logout, name='logout'),
]