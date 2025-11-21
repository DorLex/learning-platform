from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.serializers.statistic import CourseStatisticSerializer
from courses.services.statistic import get_course_statistics


@extend_schema(tags=['Courses'])
class CoursesStatisticAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @extend_schema(responses=CourseStatisticSerializer(many=True))
    def get(self, _request: Request) -> Response:
        course_statistics: QuerySet = get_course_statistics()
        serializer: CourseStatisticSerializer = CourseStatisticSerializer(course_statistics, many=True)

        return Response(serializer.data)
