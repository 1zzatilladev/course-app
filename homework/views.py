from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Homework, HomeworkSubmission
from .serializer import HomeworkSerializer, HomeworkSubmissionSerializer

class HomeworkViewSet(ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Homework.objects.all()
        return Homework.objects.filter(is_active=True)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  
        return [IsAuthenticated()]  

class HomeworkSubmissionViewSet(ModelViewSet):
    serializer_class = HomeworkSubmissionSerializer
    queryset = HomeworkSubmission.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return HomeworkSubmission.objects.all()
        return HomeworkSubmission.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)