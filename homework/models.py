from django.db import models
from lesson.models import Lesson
from users.models import User
# Create your models here.


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to='homeworks/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descriptions = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='submissions/', blank=True, null=True)
    ball = models.IntegerField(default=0)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)