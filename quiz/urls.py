from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/quizzes/',
         views.quiz_list, name='quiz_list'),
    path('take/<int:quiz_id>/',
         views.take_quiz, name='take_quiz'),
    path('result/<int:quiz_id>/',
         views.quiz_result, name='quiz_result'),
]