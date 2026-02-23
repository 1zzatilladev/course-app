from django.contrib import admin
from .models import StudentCourse, StudentLessonProgress, StudentLessonFeedback
# Register your models here.


admin.site.register(StudentLessonFeedback)
admin.site.register(StudentLessonProgress)
admin.site.register(StudentCourse)