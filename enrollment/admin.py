# enrollment/admin.py

from django.contrib import admin
from .models import Enrollment, Payment
# Register your models here.

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'enrolled_at')
    list_filter = ('status',)
    search_fields = ('student__username', 'course__title')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'amount', 'status', 'payment_date')
    list_filter = ('status',)
    search_fields = ('enrollment__student__username',)