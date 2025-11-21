from django.urls import URLPattern, path

from lessons.views.lesson import LessonAPIView
from lessons.views.lessons import LessonsWithInfoAPIView

urlpatterns: list[URLPattern] = [
    path('lessons/', LessonsWithInfoAPIView.as_view()),
    path('lessons/<int:lesson_id>', LessonAPIView.as_view()),
]
