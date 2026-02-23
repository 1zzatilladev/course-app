from django.db import models
from course.models import Module
# Create your models here.


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)