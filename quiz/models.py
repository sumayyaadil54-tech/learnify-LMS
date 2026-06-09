from django.db import models
from usersapp.models import CustomUser
from courses.models import Course
# Create your models here.

class Quiz(models.Model):
    course = models.ForeignKey(Course,
                              on_delete=models.CASCADE,
                              related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    pass_percentage = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,
                            on_delete=models.CASCADE,
                            related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text[:50]

class StudentScore(models.Model):
    student = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,
                            on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    percentage = models.FloatField()
    passed = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title} - {self.score}/{self.total}"