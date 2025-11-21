from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from course_catalog.permissions import IsAdminOrAuthRead
from course_catalog.serializers.course_access import CourseAccessSerializer
from course_catalog.services.course import CourseService


@extend_schema(tags=['Courses'])
class CoursesAccessAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    @extend_schema(responses=CourseAccessSerializer)
    def get(self, _request: Request) -> Response:
        course_service: CourseService = CourseService()
        courses_accesses: ReturnList = course_service.get_courses_accesses()
        return Response(courses_accesses)

    @extend_schema(
        request=CourseAccessSerializer,
        responses=CourseAccessSerializer,
    )
    def post(self, request: Request) -> Response:
        serializer: CourseAccessSerializer = CourseAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
