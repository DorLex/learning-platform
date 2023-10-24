from django.urls import path

from .views import courses_statistic_view, courses_access_view

urlpatterns = [
    path('courses-statistic/', courses_statistic_view.CoursesStatisticAPIView.as_view()),
    path('courses-access/', courses_access_view.CoursesAccessAPIView.as_view()),
]
