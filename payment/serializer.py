from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    student_course_info = serializers.CharField(source='student_course.__str__', read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']