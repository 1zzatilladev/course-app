from rest_framework.viewsets import ModelViewSet
from .models import Course, Module
from .serializer import CourseSerializer, ModuleSerializer

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
