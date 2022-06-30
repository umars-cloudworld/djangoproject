from .views import *
from django.urls import path

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('forget-password/', forget_password, name='forget_password'),
    path('logout/', logout_view, name='forget_password'),
    path('profile/', profile_view, name='profile'),
]
