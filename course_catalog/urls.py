from django.urls import path

from . import views

urlpatterns = [
    path('courses-statistic/', views.CoursesStatisticAPIView.as_view()),
]
