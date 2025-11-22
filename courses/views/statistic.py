from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from courses.serializers.statistic import CourseStatisticSerializer
from courses.services.statistic import StatisticService


@extend_schema(tags=['Courses'])
class CoursesStatisticAPIView(APIView):
    permission_classes: tuple = (IsAuthenticatedOrReadOnly,)

    @extend_schema(responses=CourseStatisticSerializer(many=True))
    def get(self, _request: Request) -> Response[ReturnList]:
        """Статистика курсов"""

        statistic_service: StatisticService = StatisticService()
        course_statistic: ReturnList = statistic_service.get_course_statistic()
        return Response(course_statistic)
