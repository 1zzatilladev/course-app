from django.db import models
from category.models import Category
# Create your models here.


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    intro_video_url = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    discount_protect = models.IntegerField(default=0)
    learned_students = models.IntegerField(default=0)
    rate = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)