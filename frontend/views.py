from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from course.models import Course, Module
from category.models import Category


class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(is_active=True).select_related('category').order_by('-created_at')[:6]
        context['categories'] = Category.objects.filter(is_active=True).order_by('title')[:8]
        return context


class CourseListView(ListView):
    model = Course
    template_name = 'frontend/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(is_active=True).select_related('category')


class CourseDetailView(DetailView):
    model = Course
    template_name = 'frontend/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = Module.objects.filter(course=self.object, is_active=True)
        context['categories'] = Category.objects.filter(is_active=True).order_by('title')[:8]
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'frontend/category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.filter(is_active=True).order_by('title')


class CategoryCourseListView(ListView):
    model = Course
    template_name = 'frontend/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(category_id=self.kwargs['pk'], is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = get_object_or_404(Category, pk=self.kwargs['pk'], is_active=True)
        context['categories'] = Category.objects.filter(is_active=True).order_by('title')[:8]
        return context
