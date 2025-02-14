from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from course_catalog.serializers.courses_statistic import CourseStatisticsSerializer
from course_catalog.services.courses_statistic import get_course_statistics


class CoursesStatisticAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request: Request):
        course_statistics: QuerySet = get_course_statistics()
        serializer = CourseStatisticsSerializer(course_statistics, many=True)

        return Response(serializer.data)
