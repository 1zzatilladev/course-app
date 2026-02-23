from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)  
router.register('modules', ModuleViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]