from django.urls import path

from .views import lessons_views, lesson_views

urlpatterns = [
    path('lessons/', lessons_views.LessonsAPIView.as_view()),
    path('by-course/<int:course_id>/lessons/', lessons_views.LessonsByCourseAPIView.as_view()),
    path('lessons/<int:lesson_id>/', lesson_views.LessonAPIView.as_view()),
]
