from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category
from .serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  
        return [IsAuthenticated()] 
    
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Category.objects.filter(is_active=True)
        return Category.objects.all()