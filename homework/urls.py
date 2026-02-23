from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, HomeworkSubmissionViewSet

router = DefaultRouter()
router.register('list', HomeworkViewSet)  
router.register('submissions', HomeworkSubmissionViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]