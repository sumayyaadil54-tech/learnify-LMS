from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .models import Enrollment, Payment
# Create your views here.

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Check if already enrolled
    already_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()
    
    if already_enrolled:
        messages.warning(request, 'You are already enrolled!')
        return redirect('my_courses')
    
    if request.method == 'POST':
        # Create enrollment
        enrollment = Enrollment.objects.create(
            student=request.user,
            course=course,
            status='active'
        )
        # Create payment record
        Payment.objects.create(
            enrollment=enrollment,
            amount=course.price,
            status='completed'
        )
        messages.success(request, 
                        f'Successfully enrolled in {course.title}!')
        return redirect('my_courses')
    
    return render(request, 'enrollment/enroll_confirm.html', {
        'course': course
    })

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(
        student=request.user
    ).select_related('course')
    return render(request, 'enrollment/my_courses.html', {
        'enrollments': enrollments
    })

@login_required
def cancel_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment,
                                  id=enrollment_id,
                                  student=request.user)
    if request.method == 'POST':
        enrollment.status = 'cancelled'
        enrollment.save()
        messages.success(request, 'Enrollment cancelled!')
        return redirect('my_courses')
    return render(request, 'enrollment/cancel_confirm.html', {
        'enrollment': enrollment
    })