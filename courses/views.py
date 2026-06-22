# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Category,Lesson
from .forms import CourseForm, CategoryForm

# Create your views here.

def home(request):
    courses = Course.objects.filter(
                status='published').order_by('-created_at')[:6]
    categories = Category.objects.all()
    return render(request, 'courses/home.html', {
        'courses': courses,
        'categories': categories
    })

def course_list(request):
    courses = Course.objects.filter(status='published')
    categories = Category.objects.all()
    
    # Search
    query = request.GET.get('q')
    if query:
        courses = courses.filter(title__icontains=query)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        courses = courses.filter(category_id=category_id)
    
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'categories': categories,
        'query': query
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons
    })
    
def lesson_detail(request,pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson
    })

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            messages.success(request, 'Course created!')
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', 
                 {'form': form})
    
    @login_required
    def course_list(request):
       return render(request, 'courses/course_list.html', context)
   