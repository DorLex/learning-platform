from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'lessons', views.LessonsViewSet, basename='lesson')

urlpatterns = [
    path('courses/<int:course_id>/lessons', views.LessonsByCourseViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
