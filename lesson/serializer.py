from rest_framework import serializers
from .models import Lesson
from course.models import Module

class LessonSerializer(serializers.ModelSerializer):
    module_title = serializers.CharField(source='module.title', read_only=True)
    course_title = serializers.CharField(source='module.course.title', read_only=True)
    
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']