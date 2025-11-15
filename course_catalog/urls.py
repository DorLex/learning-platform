from django.urls import URLPattern, path

from course_catalog.views.courses_access import CoursesAccessAPIView
from course_catalog.views.courses_statistic import CoursesStatisticAPIView

urlpatterns: list[URLPattern] = [
    path('courses-statistic/', CoursesStatisticAPIView.as_view()),
    path('courses-access/', CoursesAccessAPIView.as_view()),
]
