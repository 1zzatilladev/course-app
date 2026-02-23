from django.db import models
from users.models import User
from student.models import StudentCourse
# Create your models here.


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CART = 'cart', 'Cart'
        CASH = 'cash', 'Cash'
        CLICK = 'click', 'Click'
        PAYME = 'payme', 'Payme'
        COIN = 'coin', 'Coin'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    student_course = models.ForeignKey(StudentCourse, on_delete=models.SET_NULL, null=True)
    payment_type = models.CharField(max_length=10, choices=PaymentType.choices)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)