from django.urls import path

from course_catalog.views.courses_access import CoursesAccessAPIView
from course_catalog.views.courses_statistic import CoursesStatisticAPIView

urlpatterns = [
    path('courses-statistic/', CoursesStatisticAPIView.as_view()),
    path('courses-access/', CoursesAccessAPIView.as_view()),
]
