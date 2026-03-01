from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Homework, HomeworkSubmission
from .serializer import HomeworkSerializer, HomeworkSubmissionSerializer

class HomeworkViewSet(ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    
 

class HomeworkSubmissionViewSet(ModelViewSet):
    serializer_class = HomeworkSubmissionSerializer
    queryset = HomeworkSubmission.objects.all()
    
