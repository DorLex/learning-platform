from django.urls import path

from educational_content.views.lesson import LessonAPIView
from educational_content.views.lessons import LessonsWithInfoAPIView, LessonsWithInfoByCourseAPIView

urlpatterns = [
    path('lessons/', LessonsWithInfoAPIView.as_view()),
    path('by-course/<int:course_id>/lessons/', LessonsWithInfoByCourseAPIView.as_view()),
    path('lessons/<int:lesson_id>/', LessonAPIView.as_view()),
]
