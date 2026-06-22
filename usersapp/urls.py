# usersapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # The empty string here means it handles the base landing page
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]