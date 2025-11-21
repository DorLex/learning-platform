from django.urls import URLPattern, path

from courses.views.courses_access import CourseAccessAPIView
from courses.views.courses_statistic import CoursesStatisticAPIView

urlpatterns: list[URLPattern] = [
    path('statistic/', CoursesStatisticAPIView.as_view()),
    path('access/', CourseAccessAPIView.as_view()),
]
