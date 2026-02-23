from rest_framework.serializers import ModelSerializer
from .models import StudentCourse, StudentLessonFeedback, StudentLessonProgress



class StudentCourseserializer(ModelSerializer):

    class Meta:
        model = StudentCourse
        fields = '__all__'




class StudentLessonFeedbackserializer(ModelSerializer):

    class Meta:
        model = StudentLessonFeedback
        fields = '__all__'





class StudentLessonProgressserializer(ModelSerializer):

    class Meta:
        model = StudentLessonProgress
        fields = '__all__'