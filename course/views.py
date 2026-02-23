from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course, Module
from .serializer import CourseSerializer, ModuleSerializer

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()] 
        return [IsAuthenticated()]  
    
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Course.objects.filter(is_active=True)
        return Course.objects.all()

class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  
        return [IsAuthenticated()] 
    
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Module.objects.filter(is_active=True)
        return Module.objects.all()