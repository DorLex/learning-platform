from django.urls import path

from . import views

urlpatterns = [
    path('lessons/', views.LessonsAPIView.as_view()),
    path('by-course/<int:course_id>/lessons/', views.LessonsByCourseAPIView.as_view()),
]
