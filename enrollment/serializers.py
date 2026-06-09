from rest_framework import serializers
from .models import Enrollment, Payment

class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(
        source='course.title', read_only=True)
    student_name = serializers.CharField(
        source='student.username', read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'