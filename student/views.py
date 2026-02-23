from rest_framework.viewsets import ModelViewSet
from .serializer import StudentCourseserializer, StudentLessonFeedbackserializer, StudentLessonProgressserializer
from .models import StudentCourse, StudentLessonProgress, StudentLessonFeedback
from rest_framework.permissions import IsAuthenticated

# Create your views here.




class StudentCourseViewSet(ModelViewSet):
    serializer_class = StudentCourseserializer
    queryset = StudentCourse.objects.all()
    permission_classes = [IsAuthenticated]



class StudentLessonFeedbackViewSet(ModelViewSet):
    serializer_class = StudentLessonFeedbackserializer
    queryset = StudentLessonFeedback.objects.all()
    permission_classes = [IsAuthenticated]




class StudentLessonProgressViewSet(ModelViewSet):
    serializer_class = StudentLessonProgressserializer
    queryset = StudentLessonProgress.objects.all()
    permission_classes = [IsAuthenticated]
    
