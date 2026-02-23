from rest_framework import serializers
from .models import Homework, HomeworkSubmission
from lesson.models import Lesson
from users.models import User

class HomeworkSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    
    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']



class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    homework_title = serializers.CharField(source='homework.title', read_only=True)
    
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']