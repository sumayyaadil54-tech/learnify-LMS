# enrollment/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('enroll/<int:course_id>/', 
         views.enroll_course, name='enroll_course'),
    path('my-courses/', 
         views.my_courses, name='my_courses'),
    path('cancel/<int:enrollment_id>/', 
         views.cancel_enrollment, name='cancel_enrollment'),
]