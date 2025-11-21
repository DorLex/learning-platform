from django.urls import URLPattern, path

from lessons.views.lesson import LessonAPIView
from lessons.views.lessons import LessonsAPIView

urlpatterns: list[URLPattern] = [
    path('', LessonsAPIView.as_view()),
    path('<int:lesson_id>', LessonAPIView.as_view()),
]
