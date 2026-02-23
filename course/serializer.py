from rest_framework import serializers
from .models import Course, Module
from category.models import Category

class ModuleSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Module
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']




class CourseSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    modules_count = serializers.IntegerField(source='modules.count', read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'learned_students', 'rate']