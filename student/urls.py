from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentCourseViewSet, 
    StudentLessonProgressViewSet, 
    StudentLessonFeedbackViewSet
)

router = DefaultRouter()
router.register('courses', StudentCourseViewSet)
router.register('progress', StudentLessonProgressViewSet)
router.register('feedback', StudentLessonFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]