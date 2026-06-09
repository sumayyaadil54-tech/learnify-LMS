from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.api_views import CategoryViewSet, CourseViewSet, LessonViewSet
from enrollment.api_views import EnrollmentViewSet, PaymentViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('enrollments', EnrollmentViewSet, basename='enrollment')
router.register('payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]