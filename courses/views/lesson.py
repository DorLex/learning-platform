from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from courses.serializers.lesson import LessonWithInfoByCourseSerializer
from courses.services.course import CourseService


@extend_schema(tags=['Courses'])
class LessonsByCourseAPIView(APIView):
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(responses=LessonWithInfoByCourseSerializer(many=True))
    def get(self, request: Request, course_id: int) -> Response[ReturnList]:
        """Список уроков курса, доступного пользователю, с информацией о просмотрах"""

        course_service: CourseService = CourseService()
        lessons: ReturnList = course_service.get_course_lessons_by_user(course_id, request.user)
        return Response(lessons)
