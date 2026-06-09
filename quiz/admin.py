from django.contrib import admin
from .models import Quiz, Question, StudentScore

# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'pass_percentage', 'created_at')
    search_fields = ('title',)
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'correct_answer')
    search_fields = ('question_text',)

@admin.register(StudentScore)
class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 
                   'total', 'percentage', 'passed')
    list_filter = ('passed',)