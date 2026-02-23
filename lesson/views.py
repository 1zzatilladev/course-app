from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Lesson
from .serializer import LessonSerializer

class LessonViewSet(ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  
        return [IsAuthenticated()]  
    
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Lesson.objects.filter(is_active=True)
        return Lesson.objects.all()