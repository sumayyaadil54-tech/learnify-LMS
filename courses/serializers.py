from rest_framework import serializers
from .models import Category, Course, Lesson

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    category_name = serializers.CharField(
        source='category.name', read_only=True)
    instructor_name = serializers.CharField(
        source='instructor.username', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'