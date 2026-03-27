# users/urls.py
from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', register_view, name='register'),
    path("login/", views.login_view, name="login"),
    path('', views.home, name='home'),
]



