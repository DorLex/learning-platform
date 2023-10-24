from django.urls import path

from .views import lessons_view, one_lesson_view

urlpatterns = [
    path('lessons/', lessons_view.LessonsWithInfoAPIView.as_view()),
    path('by-course/<int:course_id>/lessons/', lessons_view.LessonsWithInfoByCourseAPIView.as_view()),
    path('lessons/<int:lesson_id>/', one_lesson_view.LessonAPIView.as_view()),
]
