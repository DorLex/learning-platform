from django.urls import path, URLPattern

from educational_content.views.lesson import LessonAPIView
from educational_content.views.lessons import LessonsWithInfoAPIView, LessonsWithInfoByCourseAPIView

urlpatterns: list[URLPattern] = [
    path('lessons/', LessonsWithInfoAPIView.as_view()),
    path('by-course/<int:course_id>/lessons/', LessonsWithInfoByCourseAPIView.as_view()),
    path('lessons/<int:lesson_id>', LessonAPIView.as_view()),
]
