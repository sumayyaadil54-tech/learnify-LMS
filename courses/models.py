# courses/models.py

from django.db import models
from usersapp.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, 
                                on_delete=models.CASCADE,
                                related_name='courses')
    instructor = models.ForeignKey(CustomUser,
                                  on_delete=models.CASCADE,
                                  related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', 
                                 blank=True, null=True)
    level = models.CharField(max_length=20, 
                            choices=LEVEL_CHOICES, 
                            default='beginner')
    status = models.CharField(max_length=20,
                             choices=STATUS_CHOICES,
                             default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course,
                              on_delete=models.CASCADE,
                              related_name='lessons')
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ['order']