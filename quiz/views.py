from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Question, StudentScore

# Create your views here.

@login_required
def quiz_list(request, course_id):
    from courses.models import Course
    course = get_object_or_404(Course, id=course_id)
    quizzes = Quiz.objects.filter(course=course)
    return render(request, 'quiz/quiz_list.html', {
        'course': course,
        'quizzes': quizzes
    })

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for question in questions:
            selected = request.POST.get(f'question_{question.id}')
            if selected == question.correct_answer:
                score += 1

        percentage = (score / total * 100) if total > 0 else 0
        passed = percentage >= quiz.pass_percentage

        StudentScore.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            total=total,
            percentage=percentage,
            passed=passed
        )
        return redirect('quiz_result', quiz_id=quiz.id)

    return render(request, 'quiz/take_quiz.html', {
        'quiz': quiz,
        'questions': questions
    })

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = StudentScore.objects.filter(
        student=request.user,
        quiz=quiz
    ).last()
    return render(request, 'quiz/quiz_result.html', {
        'quiz': quiz,
        'result': result
    })