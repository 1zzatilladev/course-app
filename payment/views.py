from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializer import PaymentSerializer

class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['payment_type', 'student_course']
    search_fields = ['user__username']
    ordering_fields = ['amount', 'created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Payment.objects.all()
        return Payment.objects.filter(user=user)