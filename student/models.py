from django.db import models
from users.models import User
from course.models import Course
from lesson.models import Lesson
# Create your models here.


class StudentCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class StudentLessonProgress(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    is_opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_homework_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class StudentLessonFeedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    star = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)