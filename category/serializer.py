from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    courses_count = serializers.IntegerField(source='courses.count', read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']