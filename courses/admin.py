from django.contrib import admin
from .models import Category, Course, Lesson
# Register your models here.

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'instructor', 
                   'price', 'level', 'status', 'created_at')
    list_filter = ('status', 'level', 'category')
    search_fields = ('title', 'description')
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    search_fields = ('title',)