from django.urls import path

from . import views

urlpatterns = [
    path('lessons/', views.LessonsViewSet.as_view({'get': 'list'})),
    path('by-course/<int:course_id>/lessons/', views.LessonsByCourseViewSet.as_view({'get': 'list'})),
]
