from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'
    
    role = models.CharField(max_length=20, choices=RoleChoices.choices, default=RoleChoices.STUDENT)
    phone_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"