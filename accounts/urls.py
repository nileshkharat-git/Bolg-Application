from django.urls import path

from .views import *

urlpatterns = [
    path('signup', user_signup, name='signup'),
    path('login', user_login, name='login'),
    path('dashboard', dash_board, name='dashBoard'),
    path('logout',user_logout, name='logout')
]
