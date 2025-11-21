from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from courses.serializers.access import CourseAccessSerializer
from courses.services.course import CourseService


@extend_schema(tags=['Courses'])
class CourseAccessAPIView(APIView):
    permission_classes: tuple = (IsAdminOrAuthRead,)

    @extend_schema(responses=CourseAccessSerializer(many=True))
    def get(self, _request: Request) -> Response[ReturnList]:
        """Список доступов Пользователь-Курс"""

        course_service: CourseService = CourseService()
        courses_accesses: ReturnList = course_service.get_courses_accesses()
        return Response(courses_accesses)

    @extend_schema(
        request=CourseAccessSerializer,
        responses=CourseAccessSerializer,
    )
    def post(self, request: Request) -> Response[ReturnDict]:
        """Создать доступ Пользователь-Курс"""

        serializer: CourseAccessSerializer = CourseAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
