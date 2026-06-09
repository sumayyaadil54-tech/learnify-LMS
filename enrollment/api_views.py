from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment, Payment
from .serializers import EnrollmentSerializer, PaymentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(
            student=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(
            enrollment__student=self.request.user)