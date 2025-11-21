from django.urls import URLPattern, path

from lessons.views.lesson import LessonAPIView
from lessons.views.lessons import LessonsWithInfoAPIView

urlpatterns: list[URLPattern] = [
    path('', LessonsWithInfoAPIView.as_view()),
    path('<int:lesson_id>', LessonAPIView.as_view()),
]
