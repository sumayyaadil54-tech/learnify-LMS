# courses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, 
         name='course_detail'),
    path('courses/create/', views.course_create, 
         name='course_create'),
    path('lessons/<int:pk>/', views.lesson_detail,
         name='lesson_detail'),
]