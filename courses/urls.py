from django.urls import URLPattern, path

from courses.views.access import CourseAccessAPIView
from courses.views.lesson import LessonsByCourseAPIView
from courses.views.statistic import CoursesStatisticAPIView

urlpatterns: list[URLPattern] = [
    path('statistic/', CoursesStatisticAPIView.as_view()),
    path('access/', CourseAccessAPIView.as_view()),
    path('<int:course_id>/lessons/', LessonsByCourseAPIView.as_view()),
]
